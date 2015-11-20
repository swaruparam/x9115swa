import random
import math
import sys
from sk import a12

def type1(can_x,can_y):
  if can_x.can_energy() < can_y.can_energy():
    return 1
  else:
    return 0
    
def type2(prev_era,curr_era):
  improvement = a12(curr_era,prev_era)
  if improvement > 0.5:
    return 5
  else:
    return -1
    
def loss_in_eras(first_era, last_era):
  loss = [ ]
  if len(first_era) != len(last_era):
    min_length = min(len(first_era),len(last_era))
    first_era = first_era[:min_length]
    last_era = last_era[:min_length]
  for i,j in zip(first_era,last_era):
    loss.append(i-j)
  return loss
  
# prob for SA
def prob(currEnergy, neighborEnergy, t):
    p = (currEnergy-neighborEnergy)/t
    ret = math.exp(p)
    return ret

# normalization and denormalization of energies
def norm(curr_energy,min_energy,max_energy):
    return (curr_energy-min_energy)/(max_energy-min_energy)

def denorm(curr_energy,min_energy,max_energy):
    return (max_energy-min_energy)*curr_energy + min_energy

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
    best_energy = energycan
    for _ in range(steps): # iterating through number of defined steps
      if next_can.ok() == True: # if generated output meets constraints
        new_energy = next_can.can_energy()
        if new_energy < best_energy:  # update best energy
          best_energy = new_energy
      next_can.decs[index]-=step
    if best_energy == energycan:
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
    eb = norm(sb.can_energy(),min_energy,max_energy)
    e = norm(s.can_energy(),min_energy,max_energy)
    k = 1.0
    out = [ ]
    curr_era = [ ]
    prev_era = [ ]
    lives = 5
        
    while k < kmax and lives > 0:
            
        sn = obj()
        en = norm(sn.can_energy(),min_energy,max_energy)

        if type1(sn,sb):
            sb.copy(sn)
            eb = en
            curr_era.append(sn.can_energy())
            out.append("!")
        
        if type1(sn,s): # 1 if en < e
            s.copy(sn)
            e = en
            out.append("+")
            
        elif prob(e,en, (k/kmax)*5) < random.random():
            s.copy(sn)
            e = en
            out.append("?")
            
        else:
            out.append(".")
        
        curr_era.append(s.can_energy())
            
        if k%25 == 0:
           print int(k), " - ",
           print "".join(out)
           #print curr_era
           if prev_era == [ ]:
             first_era = curr_era[:]
           prev_era = curr_era[:]
           lives = lives + type2(prev_era,curr_era)
           curr_era = [ ]
           out = [ ]
        
        k = k+1 
                
    #print "\nKmax = ", kmax
    #print "Baseline = 1000", 
    #print "Cooling = 5"
    
    loss = loss_in_eras(first_era, prev_era)
    print "Loss numbers: " , loss
    print_can = [ ]
    for can in sb.decs:
     print_can.append(round(can,3))    
    print "Best candidate: ", print_can
    best_en = denorm(eb,min_energy,max_energy)
    best_en_rounded = round(best_en,4)
    print "Best energy = " , best_en_rounded
    return prev_era, best_en

def maxWalkSat(obj):
    # setting parameters
    max_tries = 25
    max_changes = 100
    p = 0.5
    best_can = obj()
    min_energy, max_energy = best_can.baseline_study()
    threshold = 1
    best_energycan = norm(best_can.can_energy(),min_energy,max_energy)
    curr_era = [ ]
    prev_era = [ ]
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
        energycan = norm(can.can_energy(),min_energy,max_energy)
        # if set threshold is met, break
        if energycan > threshold:
          best_can.copy(can)
          best_energycan = energycan
          flag = 1
          break
        
        index = random.randint(0, can.no_decs-1)
        if p < random.random():
          # mutate randomly
          can = randomChange(can,index, obj)
          energycan = norm(can.can_energy(),min_energy,max_energy)
          out.append("?")
          curr_era.append(can.can_energy())
        
                
        else:
          # mutate to get best energy
          new_can = bestChange(can,index,energycan,obj)
          new_energycan = norm(new_can.can_energy(),min_energy,max_energy)
          #if new_energycan < energycan:
          if type1(new_can,can):
            energycan = new_energycan
            can.copy(new_can)
            out.append("+")
            curr_era.append(can.can_energy())
        
        
        # updating best energy 
        #if energycan < best_energycan:
        if type1(can,best_can):
          best_energycan = energycan
          best_can.copy(can)
          out.append("!")
          curr_era.append(best_can.can_energy())
        
        out.append(".")
        curr_era.append(can.can_energy())
        
        if i%25 == 0:
          print i, 
          print "".join(out)
          if prev_era == [ ]:
             first_era = curr_era[:]
          prev_era = curr_era[:]
          lives = lives + type2(prev_era,curr_era)
          curr_era = [ ]
          out = [ ]
      
    loss = loss_in_eras(first_era, prev_era)
    print "Loss numbers: " , loss    
    print_can = [ ]
    for can in best_can.decs:
     print_can.append(round(can,3))    
    print "Best candidate: ", print_can
    best_energycan = denorm(best_energycan,min_energy,max_energy)
    best_energycan_rounded = round(best_energycan,4)
    print "Best energy: ", best_energycan_rounded
    return prev_era, best_energycan
    
def differentialEvolution(obj):
    k=0
    repeats = 10
    no_cans = 100
    extrapolate_amt = 0.75
    prob_crossover = 0.3
    epsilon = 0.01
    
    can1 = obj()
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
      f1,f2 = can.eval_can()
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
      if can.can_energy() > best_can.can_energy():
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
        curr_era.append(new_can.can_energy())
        
        k = k+1
        if k%50 == 0:
          print k, 
          print "".join(out)
          if prev_era == [ ]:
            first_era = curr_era[:]
          prev_era = curr_era[:]
          lives = lives + type2(prev_era,curr_era)
          curr_era = [ ]
          out = [ ]
    
    loss = loss_in_eras(first_era, prev_era)
    print "Loss numbers: " , loss     
    print_can = [ ]
    for can in best_can.decs:
     print_can.append(round(can,3))    
    print "Best candidate: ", print_can
    best_energycan_rounded = round(best_can.can_energy(),4)
    print "Best energy: ", best_energycan_rounded
    print "Aggregated score: ", de_energy(best_can,min_f,max_f)
    return prev_era, best_can.can_energy()

  
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