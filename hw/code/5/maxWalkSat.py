import random

# Osyczka2 model class
class Osyczka2():
  
  def __init__(self):
    self.minDecs = [0, 0, 1, 0, 1, 0]
    self.maxDecs = [10, 10, 5, 6, 5, 10]
    self.lowestEnergy = -1
    self.highestEnergy = 1
    self.steps = 1000
  
  # obtaining random input x
  def evalInput(self):
    while 1:
      x = [ ]
      for i in range(6):
        xi = random.uniform(self.minDecs[i], self.maxDecs[i])
        x.append(xi)
      if self.ok(x):
        return x
  
  # returns energy f1+f2 based on Osyczka2 model
  def osyczka2_model(self,x):
    f1 = -(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)**2)*((x[3]-4)**2) + (x[4]-1)**2) 
    f2 = sum(xi**2 for xi in x)
    return f1 + f2
    
  # normalizes energy based on obtained minimum and maximum energy values  
  def norm(self,energy):
    return (energy-self.lowestEnergy)/(self.highestEnergy-self.lowestEnergy)
    
  # baseline study to obtain minimum and maximum energy values  
  def minmaxEnergy(self, n):
    for _ in range(n):
      x = self.evalInput()
      en = self.osyczka2_model(x)
      if en < self.lowestEnergy:
        self.lowestEnergy = en
      if en > self.highestEnergy:
        self.highestEnergy = en
    return (self.lowestEnergy, self.highestEnergy)
    
  # checking constraints  
  def ok(self,x):
    if x[0]+x[1]-2 < 0:
      return False
    if 6-x[0]-x[1] < 0:
      return False
    if 2-x[1]+x[0] < 0:
      return False
    if 2-x[0]+3*x[1] < 0:
      return False
    if 4-(x[2]-3)**2-x[3] < 0:
      return False
    if (x[4]-3)**3 +x[5]-4 < 0:
      return False
    return True
    
  # mutating randomly when prob is low    
  def randomChange(self,can,index):
    k=1
    kmax = 1000
    orig_can = can[:]
    randomValue = random.uniform(self.minDecs[index], self.maxDecs[index]) 
    can[index] = randomValue # initializing random value
    while self.ok(can) == True: # iterate till generated input is valid
      k=k+1
      if k == kmax: # break when threshold limit is reached
        return can
      randomValue = random.uniform(self.minDecs[index], self.maxDecs[index])
      can[index] = randomValue
    return orig_can
  
  # mutating to obtain best energy when prob is higher  
  def bestChange(self,can,index,energycan_norm):
    step = (self.maxDecs[index]-self.minDecs[index])/float(self.steps) # breaking limit into a number of steps
    new_can = can[:]
    new_can[index] = self.minDecs[index] # setting minimum value
    best_energy = energycan_norm
    for _ in range(self.steps): # iterating through number of defined steps
      if self.ok(new_can) == True: # if generated output meets constraints
        new_energy = self.norm(self.osyczka2_model(new_can))
        if new_energy > best_energy:  # update best energy
          best_energy = new_energy
      new_can[index]+=step
    if best_energy == energycan_norm:
      return can, energycan_norm
    return new_can, best_energy
    
# MaxwalkSat function starts here
def mws(model):
    # setting parameters
    max_tries = 100
    max_changes = 50
    threshold = 0.98
    p = 0.5
    best_can = model.evalInput()
    best_energycan = minEnergy
    out = [ ]
    i = 0
    
    for _ in range(max_tries): # for number of tries
      can = model.evalInput()
      energycan = model.osyczka2_model(can)
      energycan_norm = model.norm(energycan)
       
      for _ in range(max_changes): # for number of changes
        i += 1
        
        # if set threshold is met, break
        if energycan_norm > threshold:
          return can, energycan_norm
        
        index = random.randint(0,5)
        if p < random.random():
          # mutate randomly
          can = model.randomChange(can,index)
          energycan_norm = model.norm(model.osyczka2_model(can))
          out.append("?")
                
        else:
          # mutate to get best energy
          new_can, new_energycan_norm = model.bestChange(can,index,energycan_norm)
          if new_energycan_norm > energycan_norm:
            energycan_norm = new_energycan_norm
            can = new_can[:]
            out.append("+")
        
        # updating best energy 
        if energycan_norm > best_energycan:
          best_energycan = energycan_norm
          best_can = can
          out.append("!")
        
        out.append(".")
        
        if i%25 == 0:
          print i, " - ", round(best_energycan,3),
          print "".join(out)
          out = [ ]
            
    return best_can,best_energycan


model = Osyczka2()
(minEnergy, maxEnergy) = model.minmaxEnergy(5000)

(best_can, best_energycan) = mws(model)

print "Lowest Energy: ", minEnergy
print "Highest Energy: ", maxEnergy
new_can = [ ]
for can in best_can:
  new_can.append(round(can,3))
best_can = new_can[:]
print "Best Candidate: ", best_can
print "Best Energy: ", round(best_energycan,4)