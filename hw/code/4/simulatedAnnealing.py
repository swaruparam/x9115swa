import random
import math
import timeit

class simAnneal():
    
    #initializing min and max energies as 0 and 1 initially
    def __init__ (self):
        self.energyMin = 0
        self.energyMax = 1
    
    #calculation of f1    
    def schaffer1(self,x):
        return x**2
    
    #calculation of f2
    def schaffer2(self,x):
        return (x-2)**2
    
    #computing min and max energies with a baseline run of 1000    
    def energyMinMax(self):
        for it in range(1000):
            x = random.random()
            newEnergy = self.schaffer1(x) + self.schaffer2(x)
            if newEnergy < self.energyMin:
                self.energyMin = newEnergy
            if newEnergy > self.energyMax:
                self.energyMax = newEnergy
    
    #adding f1 and f2 and return normalized energy
    def normEnergy(self,x):
        en = self.schaffer1(x) + self.schaffer2(x)
        return (en-self.energyMin) / (self.energyMax-self.energyMin)
    
    #probability function    
    def prob(self, currEnergy, neighborEnergy, t):
        p = (currEnergy-neighborEnergy)/t
        ret = math.e**p
        return ret
    
    #simulated annealing starts    
    def simulatedAnnealing(self):
        print "Schaffer\n"
        kmax = 1000.0
        emax = 0        
        sb = s = random.random()
        eb = e = self.normEnergy(s)
        k = 1.0
        out = [ ]
        
        while k < kmax and e > emax:
            
            sn = random.random()
            en = self.normEnergy(sn)
 
            if en < eb:
                sb = sn
                eb = en
                out.append("!")
            
            elif en < e:
                s = sn
                e = en
                out.append("+")
            
            elif self.prob(e,en, (k/kmax)*5) < random.random():
                s = sn
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
        print "Best state = ", sb
        print "Best energy = %02f" % eb
                
start = timeit.default_timer()

sa = simAnneal()
sa.energyMinMax()
sa.simulatedAnnealing()

stop = timeit.default_timer()
time = stop - start 

print "Runtime = ", time