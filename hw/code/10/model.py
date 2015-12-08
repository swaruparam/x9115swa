import math
import random
from ga import ga
from dtlz import Model, dtlz

class ga_model():
    
    def __init__(self,base_min,base_max,basepop):
        self.mutation_options = [4,5,6]
        self.crossover_options = [1,2,3]
        self.candidates_options = [300,500,700]
        self.generations_options = [75,100,125]  
        self.no_decs = 4
        self.decs = [-1,-1,-1,-1]
        self.any_can()
        self.no_objs = 1
        self.base_min = base_min
        self.base_max = base_max
        self.basepop = basepop


    def any_can(self):
        self.decs[0] = random.choice(self.mutation_options)
        self.decs[1] = random.choice(self.crossover_options)
        self.decs[2] = random.choice(self.candidates_options)
        self.decs[3] = random.choice(self.generations_options) 
        #print "new decs", self.decs 
        return self.decs      
        
    def copy(self,other):
        self.no_decs = other.no_decs
        self.no_objs = other.no_objs
        self.decs = other.decs[:]
        
    def objectives(self):
        model = dtlz(10, 2, 1)
        print "Calling GA with decs", self.decs
        calculated_objs = ga(model, self.base_min, self.base_max, self.basepop, self.decs[2], self.decs[3], self.decs[0], self.decs[1]) #args = (candidates, generation, mutation, crossover)
        #print "new objs", calculated_objs
        return calculated_objs
    

        