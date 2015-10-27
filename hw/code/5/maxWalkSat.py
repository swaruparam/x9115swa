import random

x = [0, 0, 0, 0, 0, 0]

class maxwalkSat:
  
  def __init__(self):
    self.minValues = [0, 0, 1, 0, 1, 0]
    self.maxValues = [10, 10, 5, 6, 5, 10]
    self.lowestEnergy = 0
    self.highestEnergy = 1
    self.max_tries = 1000
    self.max_changes = 100
    self.threshold = 1.5
    self.p = 0.5
    self.steps = 10
  
  def evalInput(self):
    for i in range(6):
      xi = random.randint(self.minValues[i], self.maxValues[i])
      x[i] = xi
    return x
  
  def evalEnergy(self,x):
    f1 = -(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)**2)*((x[3]-4)**2) + (x[4]-1)**2) 
    f2 = sum(xi**2 for xi in x)
    return f1 + f2
    
  def norm(self,energy):
    return (energy-self.lowestEnergy)/(self.highestEnergy-self.lowestEnergy)
    
  def minmaxEnergy(self, n):
    for _ in range(n):
      x = self.evalInput()
      en = self.evalEnergy(x)
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
    kmax = 10
    orig_can = can
    while 1 and k<kmax:
      k=k+1
      randomValue = random.randint(self.minValues[index], self.maxValues[index])
      can[index] = randomValue
      #print self.ok(can)
      if self.ok(can) == True:
        break
    return orig_can
    
  def bestChange(self,can,index):
    best_can = can
    can[index] = self.minValues[index]
    for it in range(self.steps):
      can[index] = can[index] + (self.maxValues[index]-self.minValues[index])/self.steps
      if self.ok(can) == True:
        if self.evalEnergy(can) > self.evalEnergy(best_can):
          best_can = can
    return best_can
    

  def mws(self):
    best_can = self.evalInput()
    best_energycan = self.evalEnergy(best_can)
    out = [ ]
    
    for i in range(self.max_tries):
      can = self.evalInput()
      energycan = self.evalEnergy(can)
      energycan_norm = self.norm(energycan)
      
      for j in range(self.max_changes):
        if energycan_norm > self.threshold:
          return can, energycan
          
        index = random.randint(0,5)
        if self.p < random.random():
          can = self.randomChange(can,index)
        else:
          can = self.bestChange(can,index)
        
        newEnergy = self.evalEnergy(can)
        if newEnergy < energycan_norm:
          out.append("?.")
        else:
          out.append("+.")
        
        if j%25 == 0:
          print i,j, " - ",
          print "".join(out)
          out = [ ]
      
      energy = self.norm(self.evalEnergy(can))
      if energy > best_energycan:
          best_can = can
          best_energycan = energy
          #print "!"
            
    return best_can,best_energycan



f1 = maxwalkSat()
(minEnergy, maxEnergy) = f1.minmaxEnergy(1000)
#print (minEnergy, maxEnergy)
(best_can, best_energycan) = f1.mws()
print "Best Candidate: ", best_can
print "Best Energy: ", best_energycan