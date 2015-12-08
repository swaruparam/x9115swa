from model import ga_model
import baseline
import sys
import random
from sk import rdivDemo
import cProfile
import operator

def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func

def type1(can_x,can_y):
  def bdom(can_x,can_y):
    #print "in bdom"
    bettered = 0
    if can_x>can_y: #maximization function - farthest point is better
      #print xi,yi
      bettered = 1
      return bettered
      #return 0 # not better and not equal, so worse
    return bettered
  return bdom(can_x,can_y)
    
def type2(s,prev_era,curr_era): #both are lists of lists
  if prev_era == [ ]:
    return 5
  bettered = False
  for each_obj in range(s.no_objs):
    prev_lst = [ ]
    curr_lst = [ ]
    for each_can in prev_era:
      prev_lst.append(each_can[each_obj])
    for each_can in curr_era:
      curr_lst.append(each_can[each_obj])
    prev_mean = sum(prev_lst)/len(prev_era)
    curr_mean = sum(curr_lst)/len(prev_era)
    if curr_mean-prev_mean >= 0.01*prev_mean: #curr mean improves by atleast 1%
      bettered = True
  if bettered == True:
    return 5
  else:
    return -1

@do_cprofile
def differentialEvolution(): #object is the final era of GA (differentialEvolution(ga_model))
    #print "In DE"
    k=0
    repeats = 10
    no_cans = 10
    extrapolate_amt = 0.75
    prob_crossover = 0.3
    epsilon = 0.01
    
    best_can = ga_model(base_min,base_max,basepop)
    best_d = best_can.decs
    best_o = best_can.objectives()


    min_f = sys.maxint
    max_f = -sys.maxint-1
    
    frontier = [ ]
    curr_era = [ ]
    prev_era = [ ]
    out = [ ]
    
    for _ in range(no_cans):
      solution = [ ]
      can = ga_model(base_min,base_max,basepop)
      can_d = can.decs
      #print "new decs" , can_d
      can_o = can.objectives()
      #print "obj from GA for ", i , "-", can_o
      #print f1,f2
      if can_o < min_f:
        min_f = can_o
      if can_o > max_f:
        max_f = can_o
      solution.append(can_d)
      solution.append(can_o)
      #print "sol",solution
      if frontier!= [ ]:
          print frontier[0]
      print frontier
      frontier.append(solution)
      #print "frontier at each stage"
      print frontier

      if type1(best_o,can_o):
        best_can.copy(can)
        best_o = can_o
        best_d = can_d

    #print "frontier"
    #print frontier
    
    k = 0 
    lives = 5
    
    # joining extrapolate function here
    for _ in range(repeats):
      new_frontier = [ ]
      for one in frontier:
        if lives < 1:
          break
  
        two, three, four = threeOthers(frontier, one)
        r =random.randint(0,len(one[0])-1)
        new_can = ga_model(base_min,base_max,basepop)
        newcan_d = new_can.decs
        newcan_o = new_can.objectives()
        for i in range(new_can.no_decs):
          if random.random() < prob_crossover or i==r:
            new_can.decs[i] = (int)(two[0][i]+extrapolate_amt*(three[0][i]-four[0][i]))
            newcan_d[i] = new_can.decs[i]
          else:
            new_can.decs[i] = one[0][i]
            newcan_d[i] = new_can.decs[i]

        if type1(newcan_o,best_o):
          best_can.copy(new_can)
          best_o = newcan_o
          best_d = newcan_d

        solution = (newcan_d,newcan_o)
        new_frontier.append(solution)
        #curr_era.append(new_can.objectives())
  
    print "\nBest candidate's decisions: ", best_d
    print "Best candidate's mean distance from baseline population: ", best_o , "\n"
    
    # print "Initial Era"
    # print frontier
    # print "Final Era"
    # print new_frontier

    return frontier, new_frontier

  
#Returns three different things that are not 'avoid'.
def threeOthers(frontier, avoid):
  three_others = [ ]
  ignore = [ ]
  for i,x in enumerate(frontier):
    if x[1]==avoid[1]:
      ignore.append(i)
  while 1:
    index = random.randint(0,len(frontier)-1)
    if index not in ignore:
      three_others.append(frontier[index])
    if len(three_others) == 3:
      break      
  return three_others[0], three_others[1], three_others[2]

base_min, base_max = baseline.return_baseline()
basepop = baseline.return_basepop()
#print basepop
initial_era, final_era = differentialEvolution()

data = { }
for i in range(len(final_era)): 
  label = "ga" + `i` + "-" + str(final_era[i][0]).strip('[]')
  data[label] = final_era[i][1]

#print data
sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)

print "The best configurations obtained:\n" 
for key,value in sorted_data:
	print key, "\t" , value
#print sorted_data 