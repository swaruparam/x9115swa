import random
import math

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
        
    while k < kmax:
            
        sn = obj()
        en = norm(sn.can_energy(),min_energy,max_energy)

        if en < eb:
            sb.copy(sn)
            eb = en
            out.append("!")
        
        if en < e:
            s.copy(sn)
            e = en
            out.append("+")
            
        elif prob(e,en, (k/kmax)*5) < random.random():
            s.copy(sn)
            e = en
            out.append("?")
            
        else:
            out.append(".")
            
        if k%25 == 0:
           print int(k), " - ",
           print "".join(out)
           out = [ ]
            
        k = k+1 
                
    print "\nKmax = ", kmax
    print "Baseline = 1000", 
    print "Cooling = 5"
    print "Best state = ", sb.decs
    print "Best energy = %02f" % denorm(eb,min_energy,max_energy)
    

def maxWalkSat(obj):
    # setting parameters
    max_tries = 25
    max_changes = 100
    p = 0.5
    best_can = obj()
    min_energy, max_energy = best_can.baseline_study()
    threshold = 1.2
    best_energycan = norm(best_can.can_energy(),min_energy,max_energy)
    out = [ ]
    i = 0
    flag = 0
    
    for _ in range(max_tries): # for number of tries
      can = obj()
      
      if flag == 1:
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
        
                
        else:
          # mutate to get best energy
          new_can = bestChange(can,index,energycan,obj)
          new_energycan = norm(new_can.can_energy(),min_energy,max_energy)
          if new_energycan < energycan:
            energycan = new_energycan
            can.copy(new_can)
            out.append("+")
        
        
        # updating best energy 
        if energycan < best_energycan:
          best_energycan = energycan
          best_can.copy(can)
          out.append("!")
        
        out.append(".")
        
        if i%25 == 0:
          print i, 
          print "".join(out)
          out = [ ]

    print_can = [ ]
    for can in best_can.decs:
     print_can.append(round(can,3))    
    print "Best Candidate: ", print_can
    best_energycan = round(best_energycan,4)
    best_energycan = denorm(best_energycan,min_energy,max_energy)
    print "Best Energy: ", best_energycan
    
def differentialEvolution(obj):
    k=0
    repeats = 100
    no_cans = 100
    extrapolate_amt = 0.75
    prob_crossover = 0.3
    epsilon = 0.01
    
    can1 = obj()
    best_can = obj()
    min_energy, max_energy = can1.baseline_study()
    best_energy = 1.0
    best_can.copy(can1)
    
    frontier = [ ]
    out = [ ]
    
    for _ in range(no_cans):
      can = obj()
      print can.decs
      frontier.append(can)
    
    for k in range(repeats):
      
      if k%25 == 0:
          print k, 
          print "".join(out)
          out = [ ]
      
      total, n = 0.0, 0
      for x in frontier:
        en = de_energy(x,min_energy,max_energy)
        new = extrapolate(obj,frontier,x,extrapolate_amt,prob_crossover)
      if new.can_energy() > en:
        out.append("+")
        x.copy(new)
      else:
        out.append(".")
      total += en
      n += 1
      
      
          
      #total,n = update(obj,extrapolate_amt,prob_crossover,frontier,out)
      out.append("!")
      if total/n < epsilon or total/n < best_energy: 
        best_energy = total/n
        best_can.copy(can)
        break
    
    #for c in frontier:
    #  print c.decs
    print_can = [ ]
    for can in best_can.decs:
      print_can.append(round(can,3))     
    print "Best Candidate: ", print_can
    best_energy = round(best_energy,4)
    best_energy = denorm(best_energy,min_energy,max_energy)
    print "Best Energy: ", best_energy
  
  
def extrapolate(obj,frontier,one,extrapolate_amt,prob_crossover):
  out = obj()
  out.copy(one)
  two, three, four = threeOthers(frontier,one)
  changed = False  
  for d in range(out.no_decs):
    x,y,z = two.decs[d], three.decs[d], four.decs[d]
    if random.random() < prob_crossover:
      changed = True
      new = x + extrapolate_amt*(y - z)
      if new < out.min_range[d] or new > out.max_range[d]:
          new = max(out.min_range[d],min(new,out.max_range[d]))
      out.decs[d] = new # keep in range
  if not changed:
    d = random.randint(0, out.no_decs - 1)
    out.decs[d] = two.decs[d]
  #out.score = score(out) # remember to score it
  return out 
  
#Returns three different things that are not 'avoid'.
def threeOthers(frontier, avoid):
  three_others = [ ]
  pos = [i for i,x in enumerate(frontier) if x == avoid]
  for _ in range(3):
    index = random.randint(0,len(frontier)-1)
    if index != pos:
      three_others.append(frontier[index])
  return three_others[0], three_others[1], three_others[2]
  
def de_energy(x, min_energy,max_energy):
  # This evaluates the objs and stores them candidate.scores
  en = x.can_energy()
  # Just for fun
  norm_en = norm(x,min_energy,max_energy)
  #normalized_scores = [normalize(x) for normalize, x in zip(normalizers, candidate.scores)]
  # The distance of score of each objective from hell
  hell_dist = [(1 - x) for x in normalized_scores]

  sum_of_squares = sum([x ** 2 for x in hell_dist])

  energy = 1 - (math.sqrt(sum_of_squares) / math.sqrt(len(hell_dist)))

  return energy