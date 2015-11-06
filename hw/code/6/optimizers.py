import random
import math

def prob(currEnergy, neighborEnergy, t):
    p = (currEnergy-neighborEnergy)/t
    ret = math.exp(p)
    return ret

def neighbor(curr,index,model):
    next_can = model()
    next_can.copy(curr)
    while 1:
        next_can.decs[index]=random.uniform(next_can.min_range[index], next_can.max_range[index])
        if next_can.ok(): 
            break
    return next_can
    
def randomChange(can,index,model):
    k=1
    kmax = 1000
    #orig_can = model()
    #orig_can.copy(can)
    #randomValue = random.uniform(can.min_range[index], can.max_range[index]) 
    #can.decs[index] = randomValue # initializing random value
    while 1: # iterate till generated input is valid
      k=k+1
      randomValue = random.uniform(can.min_range[index], can.max_range[index])
      can.decs[index] = randomValue
      if k==kmax or can.ok(): # break when threshold limit is reached
        return can
    #return orig_can
    
def norm(curr_energy,min_energy,max_energy):
    return (curr_energy-min_energy)/(max_energy-min_energy)

def denorm(curr_energy,min_energy,max_energy):
    return (max_energy-min_energy)*curr_energy + min_energy
    #return (max_energy-min_energy)/(curr_energy-min_energy)

def bestChange(can,index,energycan,model):
    steps = 100
    next_can = model()
    next_can.copy(can)
    step = (next_can.max_range[index]-next_can.min_range[index])/float(steps) # breaking limit into a number of steps
    next_can.decs[index] = next_can.min_range[index] # setting minimum value
    best_energy = energycan
    for _ in range(steps): # iterating through number of defined steps
      if next_can.ok() == True: # if generated output meets constraints
        new_energy = next_can.can_energy()
        if new_energy > best_energy:  # update best energy
          best_energy = new_energy
      next_can.decs[index]+=step
    if best_energy == energycan:
      return can
    return next_can

def simulatedAnnealing(obj):
    kmax = 1000.0
    #emax = 0        
    #sb = s = random.random()
    sb = obj()
    s = obj()
    sb.copy(s)
    min_energy, max_energy = sb.baseline_study()
    emax = min_energy
    #print "decs", sb.decs
    eb = norm(sb.can_energy(),min_energy,max_energy)
    #print "eb",eb
    e = norm(s.can_energy(),min_energy,max_energy)
    k = 1.0
    out = [ ]
    #print min_energy,max_energy
        
    while k < kmax: #and e > emax:
            
        sn = obj()
        #sn = neighbor(s,random.randint(0,s.no_decs-1),obj)
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
    threshold = 0.99
    p = 0.5
    #steps = 1000
    best_can = obj()
    min_energy, max_energy = best_can.baseline_study()
    best_energycan = norm(best_can.can_energy(),min_energy,max_energy)
    out = [ ]
    i = 0
    flag = 0
    
    for _ in range(max_tries): # for number of tries
      can = obj()
      # energycan = norm(can.can_energy(),min_energy,max_energy)
      #print energycan
      #energycan_norm = model.norm(energycan)
      
      if flag == 1:
        break
       
      for _ in range(max_changes): # for number of changes
        i += 1
        energycan = norm(can.can_energy(),min_energy,max_energy)
        # if set threshold is met, break
        if energycan > threshold:
          #return can, energycan
          best_can.copy(can)
          best_energycan = energycan
          flag = 1
          break
          #best_energycan = denorm(best_energycan,min_energy,max_energy)
          #return best_can,best_energycan
        
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
          if new_energycan > energycan:
            energycan = new_energycan
            can.copy(new_can)
            out.append("+")
        
        # updating best energy 
        if energycan > best_energycan:
          best_energycan = energycan
          best_can.copy(can)
          out.append("!")
        
        out.append(".")
        
        if i%25 == 0:
          print i, 
          print "".join(out)
          out = [ ]
    #return best_can,best_energycan
    print_can = [ ]
    for can in best_can.decs:
     print_can.append(round(can,3))    
    #best_can = new_can[:]
    print "Best Candidate: ", print_can
    best_energycan = round(best_energycan,4)
    print "Best Energy: ", best_energycan
    #best_energycan = denorm(best_energycan,min_energy,max_energy)
    #return best_can,best_energycan