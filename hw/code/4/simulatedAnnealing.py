#from __future__ import print_function
import random
import math

#def say(x): print(x, end="")

#upperBound = 100000
#lowerBound = -upperBound

class simAnneal(object):
    
    #upperBound = 0;
    #lowerBound = 0;
    #energyMin = energyMax = 0
    
    def __init__ (self):
        self.upperBound = 1000
        self.lowerBound = -self.upperBound
        self.energyMin = self.energyMax = 0
        
    def schaffer1(self,x):
        return x**2
    
    def schaffer2(self,x):
        return (x-2)**2
        
    def energyMinMax(self):
        x1 = random.randrange(self.lowerBound, self.upperBound)
        self.energyMin = self.schaffer1(x1) + self.schaffer2(x1)
        self.energyMax = self.schaffer1(x1) + self.schaffer2(x1)
        for ite in range(100000):
            x2 = random.randrange(self.lowerBound, self.upperBound)
            newEnergy = self.schaffer1(x2) + self.schaffer2(x2)
            if newEnergy < self.energyMin:
                self.energyMin = newEnergy
            if newEnergy > self.energyMax:
                self.energyMax = newEnergy
    
    def normEnergy(self,x):
        en = self.schaffer1(x) + self.schaffer2(x)
        return en 
        #print en, self.energyMin, self.energyMax
        #print (en-self.energyMin) / (self.energyMax-self.energyMin)
        #return (en-self.energyMin) / (self.energyMax-self.energyMin)
        
    def prob(self, currEnergy, neighborEnergy, t):
        p = float(currEnergy-neighborEnergy)/float(t)
        ret = math.exp(p)
        return ret
        
    def simulatedAnnealing(self):
        print self.energyMin
        print self.energyMax
        kmax = 1000
        #emin = 0.00000000000001
        s = random.randrange(self.lowerBound, self.upperBound)
        #print s
        sb = s
        e = self.normEnergy(s)
        #print e
        eb = e
        k = 1
        
        while k <= kmax:# and e > emin:
            
            sn = random.randrange(self.lowerBound, self.upperBound)
            en = self.normEnergy(sn)
            #print en,
            if en < eb:
                sb = sn
                eb = en
                print "!",
            
            elif en < e:
                s = sn
                e = en
                print "+",
            
            elif self.prob(e,en, float(k)/float(kmax)) < random.random():
                s = sn
                e = en
                print "?",
            
            else:
                print ".",
            
            k = k+1 
            
            if k%25 == 0:
               print "\n"
                # print "\n"
        print "best state ", sb
        print "best energy ", eb
                

sa = simAnneal()
sa.energyMinMax()
#print(sa.energyMin)
#print(sa.energyMax)
sa.simulatedAnnealing()

