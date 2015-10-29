import random

x = [0, -1, -1, -2, -1, -2, -1]

class maxwalkSat:
  
  def __init__(self):
    self.minValues = [0, 0, 1, 0, 1, 0]
    self.maxValues = [10, 10, 5, 6, 5, 10]
    self.lowestEnergy = -1
    self.highestEnergy = 1
    self.max_tries = 1000
    self.max_changes = 100
    self.threshold = 1.1
    self.p = 0.5
    self.steps = 10
  
  
  def evalInput(self):
    while(1):
      for i in range(6):
        xi = random.uniform(self.minValues[i], self.maxValues[i])
        x[i] = xi
      if self.ok(x) == True:
        break
    return x
  
  
  def osyczka2(self,x):
    f1 = -(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)**2)*((x[3]-4)**2) + (x[4]-1)**2) 
    f2 = sum(xi**2 for xi in x)
    return f1 + f2
    
    
  def norm(self,energy):
    return (energy-self.lowestEnergy)/(self.highestEnergy-self.lowestEnergy)
    
    
  def minmaxEnergy(self, n):
    for _ in range(n):
      x = self.evalInput()
      en = self.osyczka2(x)
      if en < self.lowestEnergy:
        self.lowestEnergy = en
      if en > self.highestEnergy:
        self.highestEnergy = en
    return (self.lowestEnergy, self.highestEnergy)
    
    
  def ok(self,can):
    if x[0]+x[1]-2 >= 0 and 6-x[0]-x[1] >= 0 and 2-x[1]+x[0] >=0 and 2-x[0]+3*x[1] >=0 and 4-(x[2]-3)**2-x[3] >=0 and (x[4]-3)**3 +x[5]-4 >=0:
      return True
    else:
      return False
    
      
  def randomChange(self,can,index):
    k=1
    kmax = 100
    orig_can = can
    while 1 and k<kmax:
      k=k+1
      randomValue = random.uniform(self.minValues[index], self.maxValues[index])
      can[index] = randomValue
      if self.ok(can) == True:
        break
    return orig_can
    
    
  def bestChange(self,can,index,energycan_norm):
    step = (self.maxValues[index]-self.minValues[index])/float(self.steps)
    new_can = can
    new_can[index] = self.minValues[index]
    best_energy = energycan_norm
    while new_can[index] < self.maxValues[index]:
      if self.ok(new_can) == True:
        new_energy = self.norm(self.osyczka2(new_can))
        if new_energy > best_energy:
          best_energy = new_energy
      new_can[index]+=step
    return new_can
    

  def mws(self):
    best_can = self.evalInput()
    best_energycan = minEnergy
    out = [ ]
    i = 0
    
    for _ in range(self.max_tries):
      can = self.evalInput()
      energycan = self.osyczka2(can)
      energycan_norm = self.norm(energycan)
      
      for _ in range(self.max_changes):
        i += 1
        if energycan_norm > self.threshold:
          return can, energycan_norm
          
        index = random.randint(0,5)
        if self.p < random.random():
          new_can = self.randomChange(can,index)
          new_energycan_norm = self.norm(self.osyczka2(new_can))
          if new_energycan_norm > energycan_norm:
            energycan_norm =new_energycan_norm
            can = new_can
            out.append("?")
          else:
            out.append(".")
                
        else:
          new_can = self.bestChange(can,index,energycan_norm)
          new_energycan_norm = self.norm(self.osyczka2(new_can))
          if new_energycan_norm > energycan_norm:
            energycan_norm = new_energycan_norm
            can = new_can
            out.append("+")
          else:
            out.append(".")
        
        if i%50 == 0:
          print i, " - ",
          print "".join(out)
          out = [ ]
        
        if energycan_norm > best_energycan:
          best_energycan = energycan_norm
          best_can = can
            
    return best_can,best_energycan


f = maxwalkSat()
(minEnergy, maxEnergy) = f.minmaxEnergy(5000)
print (minEnergy, maxEnergy)
(best_can, best_energycan) = f.mws()
print "Best Candidate: ", best_can
print "Best Energy: ", best_energycan