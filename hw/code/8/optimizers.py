import random
import math
import sys
from sk import a12

  
def type1(can_x,can_y):
  def bdom(can_x,can_y):
    bettered = 0
    for (xi,yi) in zip(can_x.objectives(), can_y.objectives()):
      if xi<yi:
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
    if prev_mean-curr_mean > 0.01*prev_mean: #curr mean improves by atleast 1%
      bettered = True
  if bettered == True:
    return 5
  else:
    return -1
  
# prob for SA
def prob(s,currEnergy, neighborEnergy, t):
    ret = 0
    for i in range(s.no_objs):
      p = (currEnergy[i]-neighborEnergy[i])/t
      pe = math.exp(p)
      if pe < random.random():
        ret = 1
        return ret
    return ret

# normalization and denormalization of energies
def norm(curr_energy,min_energy,max_energy):
    norm_energy = [ ]
    for i in range(len(curr_energy)):
      norm_energy.append((curr_energy[i]-min_energy[i])/(max_energy[i]-min_energy[i]))
    return norm_energy

def denorm(curr_energy,min_energy,max_energy):
    denorm_energy = [ ]
    for i in range(len(curr_energy)):
      denorm_energy.append((max_energy[i]-min_energy[i])*curr_energy[i] + min_energy[i])
    return denorm_energy

# random change when p is low, for MWS    
def randomChange(can,index,model):
    k=1
    kmax = 1000
 
    while 1: # iterate till generated input is valid
      k=k+1
      randomValue = random.uniform(can.min_range[index], can.max_range[index])
      can.decs[index] = randomValue
      if k==kmax or can.ok(): # break when threshold limit is reached
        return can

# best change when p is high, for MWS
def bestChange(can,index,energycan,model):
    steps = 100
    next_can = model()
    next_can.copy(can)
    step = (next_can.max_range[index]-next_can.min_range[index])/float(steps) # breaking limit into a number of steps
    next_can.decs[index] = next_can.max_range[index] # setting minimum value
    best_energy = energycan[:]
    for _ in range(steps-1): # iterating through number of defined steps
      if next_can.decs[index]<=next_can.min_range[index]:
        break
      if next_can.ok() == True: # if generated output meets constraints
        new_energy = next_can.objectives()
        #if new_energy < best_energy:  # update best energy
        if type1(next_can,can):
          best_energy = new_energy[:]
      next_can.decs[index]-=step
    
    flag = 1
    for i in range(can.no_objs):
      if best_energy[i] != energycan[i]:
        flag = 0
    if flag == 1:
      return can
    return next_can

def simulatedAnnealing(obj):
    # setting parameters
    kmax = 1000.0
    sb = obj()
    s = obj()
    sb.copy(s)
    min_energy, max_energy = sb.baseline_study()
    emax = min_energy
    eb = norm(sb.objectives(),min_energy,max_energy)
    e = norm(s.objectives(),min_energy,max_energy)
    k = 1.0
    out = [ ]
    curr_era = [ ]
    prev_era = [ ]
    lives = 5
        
    while k < kmax and lives > 0:
            
        sn = obj()
        en = norm(sn.objectives(),min_energy,max_energy)
        #print "best energy pair", sb.objectives()
        
        if type1(sn,sb):
            sb.copy(sn)
            eb = en[:]
            curr_era.append(sn.objectives())
            #print "!", sn.objectives()
            #curr_era.append(sn.can_energy())
            out.append("!")
        
        if type1(sn,s): # 1 if en < e
            s.copy(sn)
            e = en[:]
            out.append("+")
            
        elif prob(s,e,en, (k/kmax)*5):
            s.copy(sn)
            e = en
            out.append("?")
            
        else:
            out.append(".")
        
        #curr_era.append(s.can_energy())
        curr_era.append(s.objectives())
            
        if k%50 == 0:
           #print int(k), " - ",
           #print "".join(out)
           #print curr_era
           if prev_era == [ ]:
             first_era = curr_era[:]
           lives = lives + type2(s,prev_era,curr_era)
           prev_era = curr_era[:]
           curr_era = [ ]
           out = [ ]
        
        k = k+1 
                
    #print "\nKmax = ", kmax
    #print "Baseline = 1000", 
    #print "Cooling = 5"
    
    print_can = [ ]
    for can in sb.decs:
     print_can.append(round(can,3))    
    print "Best candidate: ", print_can
    best_en = denorm(eb,min_energy,max_energy)
    #best_en_rounded = round(best_en,4)
    print "Corresponding objectives: " , best_en
    #print "Final era ", prev_era
    return prev_era, first_era

def maxWalkSat(obj):
    # setting parameters
    max_tries = 25
    max_changes = 100
    p = 0.5
    best_can = obj()
    min_energy, max_energy = best_can.baseline_study()
    threshold = 1
    best_energycan = norm(best_can.objectives(),min_energy,max_energy)
    curr_era = [ ]
    prev_era = [ ]
    first_era = [ ]
    out = [ ]
    i = 0
    flag = 0
    lives = 5
    
    for _ in range(max_tries): # for number of tries
      can = obj()
      
      if flag == 1 or lives < 1:
        break
       
      for _ in range(max_changes): # for number of changes
        i += 1
        
        if flag == 1:
          break
        
        energycan = norm(can.objectives(),min_energy,max_energy)
        # if set threshold is met, break
        for e in energycan:
          if e > threshold:
            best_can.copy(can)
            best_energycan = energycan[:]
            flag = 1
            break
        
        index = random.randint(0, can.no_decs-1)
        if p < random.random():
          # mutate randomly
          can = randomChange(can,index, obj)
          energycan = norm(can.objectives(),min_energy,max_energy)
          out.append("?")
          curr_era.append(can.objectives())
        
        else:
          # mutate to get best energy
          new_can = bestChange(can,index,energycan,obj)
          new_energycan = norm(new_can.objectives(),min_energy,max_energy)
          #if new_energycan < energycan:
          if type1(new_can,can):
            energycan = new_energycan[:]
            can.copy(new_can)
            out.append("+")
            curr_era.append(can.objectives())
        
        
        # updating best energy 
        #if energycan < best_energycan:
        if type1(can,best_can):
          best_energycan = energycan[:]
          best_can.copy(can)
          out.append("!")
          curr_era.append(best_can.objectives())
        
        out.append(".")
        #curr_era.append(can.objectives())
        
        if i%50 == 0:
          #print i, 
          #print "".join(out)
          if prev_era == [ ]:
             first_era = curr_era[:]
          lives = lives + type2(can,prev_era,curr_era)
          prev_era = curr_era[:]
          curr_era = [ ]
          out = [ ]
      
    #loss = loss_in_eras(first_era, prev_era)
    #print "Loss numbers: " , loss    
    print_can = [ ]
    for can in best_can.decs:
     print_can.append(round(can,3))    
    print "Best candidate: ", print_can
    best_energycan = denorm(best_energycan,min_energy,max_energy)
    #best_energycan_rounded = round(best_energycan,4)
    print "Corresponding objectives: ", best_energycan
    return prev_era, first_era
    
def differentialEvolution(obj):
    k=0
    repeats = 10
    no_cans = 100
    extrapolate_amt = 0.75
    prob_crossover = 0.3
    epsilon = 0.01
    
    can1 = obj()
    # min_f, max_f = can1.baseline_study()
    
    best_can = obj()

    min_f = [sys.maxint,sys.maxint]
    max_f = [-sys.maxint-1,-sys.maxint-1]

    best_can.copy(can1)
    
    frontier = [ ]
    curr_era = [ ]
    prev_era = [ ]
    out = [ ]
    
    for _ in range(no_cans):
      can = obj()
      f1,f2 = can.objectives()
      #print f1,f2
      if f1 < min_f[0]:
        min_f[0] = f1
      if f2 < min_f[1]:
        min_f[1] = f2
      if f1 > max_f[0]:
        max_f[0] = f1
      if f2 > max_f[1]:
        max_f[1] = f2
      frontier.append(can)
      if type1(best_can,can):
      #if can.can_energy() > best_can.can_energy():
        best_can.copy(can)
    # print min_f
    # print max_f
    
    k = 0 
    lives = 5
    
    # joining extrapolate function here
    for _ in range(repeats):
      new_frontier = [ ]
      for one in frontier:
        if lives < 1:
          break
        while 1:
          two, three, four = threeOthers(frontier, one)
          r =random.randint(0,one.no_decs-1)
          new_can = obj()
          for i in range(one.no_decs):
            if random.random() < prob_crossover or i==r:
              new_can.decs[i] = two.decs[i]+extrapolate_amt*(three.decs[i]-four.decs[i])
            else:
              new_can.decs[i] = one.decs[i]
          if new_can.ok():
            break
        #if new_can.can_energy() < best_can.can_energy():
        if type1(new_can,best_can):
          best_can.copy(new_can)
          out.append("!")
        #elif new_can.can_energy() < one.can_energy():
        elif type1(new_can,one):
          out.append("+")
        else:
          out.append(".")
        new_frontier.append(new_can)
        curr_era.append(new_can.objectives())
        
        k = k+1
        if k%50 == 0:
          #print k, 
          #print "".join(out)
          if prev_era == [ ]:
            first_era = curr_era[:]
          lives = lives + type2(can,prev_era,curr_era)
          prev_era = curr_era[:]
          curr_era = [ ]
          out = [ ]
    
    #loss = loss_in_eras(first_era, prev_era)
    #print "Loss numbers: " , loss     
    print_can = [ ]
    for can in best_can.decs:
     print_can.append(round(can,3))    
    print "Best candidate: ", print_can
    best_energycan_rounded = round(best_can.can_energy(),4)
    best_energycan = best_can.objectives()
    print "Corresponding objectives: ", best_energycan
    #print "Aggregated score: ", de_energy(best_can,min_f,max_f)
    return prev_era, first_era

  
#Returns three different things that are not 'avoid'.
def threeOthers(frontier, avoid):
  three_others = [ ]
  pos = [i for i,x in enumerate(frontier) if x == avoid]
  while 1:
    index = random.randint(0,len(frontier)-1)
    if index not in pos:
      three_others.append(frontier[index])
    if len(three_others) == 3:
      break
  return three_others[0], three_others[1], three_others[2]

# to find aggregate score from hell  
def de_energy(x, min_f, max_f):
  f1,f2 = x.eval_can()
  hell = 1
  normalized_f1 = (f1-min_f[0])/(max_f[0]-min_f[0])
  normalized_f2 = (f2-min_f[1])/(max_f[1]-min_f[1])
  fromhell_f1 = (hell - normalized_f1)
  fromhell_f2 = (hell - normalized_f2)
  sum_of_squares = fromhell_f1**2 + fromhell_f2**2
  agg_score = 1 - (math.sqrt(sum_of_squares) / math.sqrt(2))
  return agg_score