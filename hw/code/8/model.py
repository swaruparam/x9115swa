import math
import random

class dtlz7():
    
    def __init__(self):
        self.min_range = [0,0,0,0,0,0,0,0,0,0]
        self.max_range = [1,1,1,1,1,1,1,1,1,1]
        self.no_decs = 10
        self.no_objs = 2
        self.decs = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.any_can()
        
    def any_can(self):
        while 1:
            for dec in range(self.no_decs):
                self.decs[dec]=random.uniform(self.min_range[dec],self.max_range[dec])
            if self.ok(): 
                break
        
    def ok(self):
        for dec in range(self.no_decs):
            if self.decs[dec] < self.min_range[dec] or self.decs[dec] > self.max_range[dec]:
                return False
        return True
        
    def copy(self,other):
        self.no_decs = other.no_decs
        self.no_objs = other.no_objs
        self.decs = other.decs[:]
        self.min_range = other.min_range[:]
        self.max_range = other.max_range[:]

    def f1(self):
        x = self.decs[:]
        f = x[0]
        return f

    def f2(self):
        x = self.decs[:]
        f2 = (1+self.g(x))*self.h(self.f1(),self.g(x),2)
        return f2
        
    def objectives(self):
        return [self.f1(), self.f2()]
    
    def can_energy(self):
        return sum(self.objectives())
    
    def g(self,x):
        s = sum(x)
        return 1+ ((9/len(x))*s)
    
    def h(self,f,g,M):
        angle = 3*math.pi*f
        return M - ((f/(1+g))* (1+math.sin(angle)))
    
    def baseline_study(self): #to find min and max energies
        empty = [ ]
        energiesOfObjs = [[ ],[ ]]
        for _ in range(1000):
            self.any_can()
            for each_obj in range(self.no_objs):
                obj_energy = self.objectives()
                energiesOfObjs[each_obj].append(obj_energy[each_obj])
  
        min_list = [ ]
        max_list = [ ]
        for each_list in energiesOfObjs:
            min_list.append(min(each_list))
            max_list.append(max(each_list))
        print "Min values of Objectives", min_list
        print "Max values of Objectives", max_list
        return [min_list, max_list]
        