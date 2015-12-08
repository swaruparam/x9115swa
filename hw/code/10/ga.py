from __future__ import division
from random import random, randrange, randint, uniform
from abc import ABCMeta, abstractmethod
from math import exp, sqrt, cos, pi, sin
import sys
from dtlz import Model, dtlz
#from plot import make_plot
import datetime
from baseline import return_baseline, return_basepop


def ga(model, b_min, b_max, b_pop, num_can, num_gen, p_mut, p_cros):
    population_size = num_can #number of candidates
    generations = num_gen #number of generations??
    p_crossover = p_cros #pick a random decision
    p_mutation = p_mut #probability for mutation
    total_decs = 10
    total_objs = 2
    base_min = b_min
    base_max = b_max

    def gt(x,y): return x > y
    def lt(x,y): return x < y

    def objs(x):
        "Returns the objectives inside x"
        return x[1] # for example

    def bdom(x,y):
        bettered = False
        for i, (xi, yi) in enumerate(zip(objs(x),objs(y))):
            if lt(xi,yi):
                bettered = True
            #if xi != yi:  
            #    return False # not better and not equal, therefor worse
        return bettered    

    def select(population):
        """
        binary domination
        """
        for i in xrange(population_size):
            if i != population_size - 1:
                if bdom(population[i], population[i+1]):
                    return population[i]
        
    def initializePopulation(base_min, base_max):
         #choose initial population
        """
        population <- initializePopulation(population_size, problem_size)
        """
        population = []
        for _ in xrange(population_size):
            candidate = model.solution(base_min, base_max)
            population.append(candidate)
            #print len(candidate)
        return population
    
    def get_best(population):
        #determine population's average fitness
        """
        sBest <- getBestSolution(population)
        """
        #Sort population on frontier
        for i in xrange(1, len(population)):
            key = population[i]
            j = i-1
            while j >= 0 and population[j][1] < key[1]:
                population[j+1] = population[j]
                j = j-1
            population[j+1] = key
        min_energy = population[0][1]
        max_energy = population[len(population)-1][1]
        avg_energy = 0
        for i in xrange(1, len(population)):
            avg_energy += population[i][1]
        avg_energy = avg_energy/len(population)
        return min_energy, max_energy, avg_energy
        
    def crossover(parent1, parent2, p_crossover):
        cut = []
        if p_crossover == 1:
            cut_point = randrange(0, total_decs)
            child1 = parent1[0][:cut_point] + parent2[0][cut_point:]
            child2 = parent2[0][:cut_point] + parent1[0][cut_point:]
        if p_crossover == 2:
            cut.append(randrange(0, total_decs))
            cut.append(randrange(0, total_decs))
            while cut[0] == cut[1]:
                cut[0] = randrange(0, total_decs)
                cut[1] = randrange(0, total_decs)
            cut.sort()
            cut_point1 = cut[0]
            cut_point2 = cut[1]
            child1 = parent1[0][:cut_point1] + parent2[0][cut_point1:cut_point2] + parent1[0][cut_point2:]
            child2 = parent2[0][:cut_point1] + parent1[0][cut_point1:cut_point2] + parent2[0][cut_point2:]
        if p_crossover == 3:
            cut.append(randrange(0, total_decs))
            cut.append(randrange(0, total_decs))
            cut.append(randrange(0, total_decs))
            while not cut[0] != cut[1] != cut[2]:
                cut[0] = randrange(0, total_decs)
                cut[1] = randrange(0, total_decs)
                cut[2] = randrange(0, total_decs)
            cut.sort()
            cut_point1 = cut[0]
            cut_point2 = cut[1]
            cut_point3 = cut[2]
            child1 = parent1[0][:cut_point1] + parent2[0][cut_point1:cut_point2] + parent1[0][cut_point2:cut_point3] + parent2[0][cut_point3:]
            child2 = parent2[0][:cut_point1] + parent1[0][cut_point1:cut_point2] + parent2[0][cut_point2:cut_point3] + parent1[0][cut_point3:]
        return child1, child2
        
    def mutate(child, p_mutation):
        rand_prob = randint(0,99)
        if rand_prob < p_mutation:
            k = randrange(0, len(child))
            child[k] = uniform(0,1)
        return child
    
    def prune(population):
        population = population[:50] + population[(len(population)-population_size+50):]
        return population

    def loss1(i, x, y):
        return x - y

    def exp_loss(i, x, y, n):
        return exp( loss1(i, x, y) / n)

    def loss(x, y):
        x, y = model.objectives(x), model.objectives(y)
        n = min(len(x), len(y))
        losses = [ exp_loss(i, x[i], y[i], n) 
                        for i, (x[i], y[i])
                            in enumerate(zip(x, y))]
        return sum(losses)/n

    def cdom(x, y):
        """x dominates y if it losses least"""       
        return x if loss(x,y) < loss(y,x) else y

    def mean_obj_vector(population):
        era_objs = []

        for i in xrange(len(population)):
            era_objs.append(population[i][1])
        
        sum_obj = [0 for _ in xrange(total_objs)] #sum_obj = [mean(f1), mean(f2), mean(f3), mean(f4)]
            
        for j in xrange(total_objs):
            temp = []
            for i in xrange(len(era_objs)):
                temp.append(era_objs[i][j])
            sum_obj[j] = sum(temp)/len(era_objs)
        return sum_obj

    def early_termination(prev_era, curr_era):
        for i in xrange(total_objs):
            if abs(curr_era[i] - prev_era[i]) < 0.01:
                return True

    def nearest_neighbor(b_min, b_max, b_pop, candidate_obj, population):
        base_min, base_max = b_min, b_max
        base_pop = b_pop
        distance_fromCan = [0 for _ in xrange(len(population))]
        for j in xrange(len(population)):
            sum_obj = [0 for _ in xrange(len(candidate_obj))]
            for i in xrange(len(candidate_obj)):
                d1 = candidate_obj[i]
                d0 = base_pop[j][1][i]
                sum_obj[i] = (d1**2 - d0**2)**2
            distance_fromCan[j] += sum_obj[i]
        for i in xrange(len(distance_fromCan)):
            distance_fromCan[i] = sqrt(distance_fromCan[i])
        return min(distance_fromCan)  

    
    def fromHell(b_min, b_max, b_pop, population):
        minDistFromCan = 0
        for j in xrange(len(population)):
            minDistFromCan += nearest_neighbor(b_min, b_max, b_pop, population[j][1], population)
        k = minDistFromCan/population_size
        return k



    def search(iter_val):
        k = 1
        prev_era = []
        curr_era = []

        #INITIAL FRONTIER
        population = initializePopulation(base_min, base_max)
        era_zero = population

        current_gen = 0
        output = " "
        avg_container = []
        max_container = []

        while(current_gen < generations ): 
            print "In GA - generation ", current_gen
            children = []
            parents = []

            #create parent population by binary tournament
            while (len(parents)) < population_size:
                parents.append(select(population))


            while(len(children)) < population_size - 1:

                for j in xrange(1, len(parents)):

                    parent1 = parents[j-1]
                    parent2 = parents[j]
                    if parent1 != None and parent2 != None:
                        while True:
                            child1, child2 = crossover(parent1, parent2, p_crossover)
                            child1 = mutate(child1, p_mutation)
                            child2 = mutate(child2, p_mutation)
                            if model.generate_chk_constraints(child1) == True:
                                break
                            if model.generate_chk_constraints(child2) == True:
                                break

                    better_child = cdom(child1, child2)
                    if better_child == child1:
                        c = (child1, model.normalized_obj(child1, base_min, base_max))
                    else:
                        c = (child2, model.normalized_obj(child2, base_min, base_max))
                    children.append(c)
                    
            for i in xrange(len(children)):
                population.append(children[i]) 

            #SORT and PRUNE using CDOM
            #print "before prune", len(population)
            for i in xrange(1, len(population)):
                key = population[i]
                j = i-1
                while j >= 0 and cdom(population[j][0], key[0])==population[j][0]:
                    population[j+1] = population[j]
                    j = j-1
                population[j+1] = key
            population = prune(population)
            #print "after prune", len(population)
            #for i in xrange(len(population)):
            #    print "can", i, "gen", current_gen, population[i][1][0], population[i][1][1], population[i][1][2]
            

            #check for early termination
            if current_gen != 0:
                if current_gen % 99 == 0:
                    prev_era = mean_obj_vector(population)
                if current_gen % 100 == 0:
                    curr_era = mean_obj_vector(population)
                    if prev_era:
                        if early_termination(prev_era, curr_era):
                            #print fromHell(b_min, b_max, b_pop, population)
                            x = fromHell(b_min, b_max, b_pop, population)
                            #return population
                            return x

            k = k + 1
            current_gen += 1
         
        #print fromHell(b_min, b_max, b_pop, population)
        #return population
        x = fromHell(b_min, b_max, b_pop, population)
        return x
         
    
    iter_val = 1
    # for i in xrange(1):
    #     pop = search(iter_val)
    #     iter_val += 1

    return search(iter_val)



# ta = datetime.datetime.now()

# model = dtlz(10, 2, 1)
# num_can = 500
# num_gen = 100
# p_mut = 5
# p_cros = 1
# print "GA parameters: \nnum_can: ", num_can, " num_gen: ", num_gen, " p_mut: ", p_mut,\
# " p_cros: ", p_cros
# base_min, base_max = return_baseline()
# base_pop = return_basepop() 
# currpop = ga(model, base_min, base_max, base_pop, num_can, num_gen, p_mut, p_cros)
# tb = datetime.datetime.now()
#print "#Run time %f" % ((ta - tb).microseconds/1000000)
     
     
     
           