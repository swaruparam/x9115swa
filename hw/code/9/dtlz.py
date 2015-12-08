from __future__ import division
from random import random, randrange, randint, uniform
from abc import ABCMeta, abstractmethod
from math import exp, sqrt, cos, pi, sin
import sys


class Model(object):
    """
    Fills in the generic candidate
    Computes objective score for each candidate
    """
    __metaclass__ = ABCMeta
    
    def __init__(self):
        """
        Initializes variable bounds for 
        - energy
        - x vector (initialized in subclass)
        """
        self.min_agg = sys.maxint
        self.max_agg = -self.min_agg
        self.min_x = 0
        self.max_x = 0
        
    def random_x_gen(self):
        """
        Generates x's in the range 
        specified by the subclass model
        Input: None
        Output: x vector
        """
        if isinstance(self.min_x, list):
            x_list = []
            for i,j in zip(self.min_x, self.max_x):
                x_list.append(uniform(i,j))
            return x_list
        else:
            x_list = [uniform(self.min_x, self.max_x)]
            return x_list

    @abstractmethod
    def generate_chk_constraints(self, x_list):
        #overridden by subclass
        """
        Generates and checks constraints
        Input: x_list
        Output: True if constraints passed/no constraints
                False if not passed
        """
        raise NotImplementedError("Must override generate_chk_constraints()")
            
    def ok(self, x_list):
        """
        Generates first solution THEN
        Generates solution in loop, till constraints passed
        Input: x_list
        Output: valid x vector
        """
        isPassed = self.generate_chk_constraints(x_list)
        while not isPassed:
            x_list = self.random_x_gen()
            isPassed = self.generate_chk_constraints(x_list)
        return x_list
        
    def aggregator(self, x_list):
        """
        Generates energy by summing all objectives got from subclass
        
        """
        agg = 0
        for obj in self.objectives(x_list): 
            agg += obj
        return agg
        
    @abstractmethod
    def objectives(self, x):
        raise NotImplementedError("Must override objectives()")
        
    def find_min_max(self, iterations = 1000):
        for _ in xrange(iterations):
            while True:
                solution = self.random_x_gen()
                if self.ok(solution):
                    break
                
            objectives_list = self.objectives(solution)
            #print "obj_list", objectives_list

            for i in xrange(len(objectives_list)):
                if objectives_list[i] > self.max_obj[i]:
                    self.max_obj[i] = objectives_list[i]
                    
                if objectives_list[i] < self.min_obj[i]:
                    self.min_obj[i] = objectives_list[i]

        #print "min",self.min_obj, "max", self.max_obj
        return self.min_obj, self.max_obj
            
    def normalize(self, energy, min_energy, max_energy):
        norm_energy = (energy - min_energy)/(max_energy - min_energy)
        return norm_energy


class dtlz(Model):
  
    def __init__(self, decisions = 10, obj = 2, id = 1):
        Model.__init__(self)
        self.min_x = [0 for _ in xrange(decisions)]
        self.max_x = [1 for _ in xrange(decisions)]
        self.min_obj = [sys.maxint for _ in xrange(obj)]
        self.max_obj = [-sys.maxint for _ in xrange(obj)]
        self.f = [0 for _ in xrange(obj)]
        self.id = id
        #print "inside", decisions, obj

        
    def objectives(self, x):
        if self.id == 1:
            return self.f1_obj_func(x)

        if self.id == 3:
            return self.f3_obj_func(x)
            
        if self.id == 5:
            return self.f5_obj_func(x)
            
        if self.id == 7:
            return self.f7_obj_func(x)

    def normalized_obj(self, x, min_obj_list, max_obj_list):
        norm_objs = []
        objs = self.objectives(x)
        for i in xrange(len(objs)):
            norm_objs.append(self.normalize(objs[i], min_obj_list[i], max_obj_list[i]))
        return norm_objs

    def generate_chk_constraints(self, x_list):
        for i in xrange(len(x_list)):
            if x_list[i] < self.min_x[i] or x_list[i] > self.max_x[i]:
                return False
        return True

    def solution(self, min_obj_list, max_obj_list):
        x = self.ok(self.random_x_gen())
        norm_objs = self.normalized_obj(x, min_obj_list, max_obj_list)
        return x, norm_objs
      
    def get_energy(self, x):
        energy = self.aggregator(x)
        return energy
          
    def g_func(self, x):
        """
        Returns the corresponding g func
        --------------------------------------------------------------------
        input: problem number 1, 3, 5, or 7
               the decision vector x
        --------------------------------------------------------------------
        output: g_func
        --------------------------------------------------------------------
        """
        if self.id == 1 or 3:
            return self.g13_func(x)

        if self.id == 5:
            return self.g5_func(x)
            
        if self.id == 7:
            return self.g7_func(x)
          
        
    def g13_func(self, x):
        y = 0.0
        for i in xrange(len(x)):
            y += ((x[i] - 0.5)**2 - cos(20*pi*(x[i] - 0.5)))
        return 100.0 * (y + len(x))
      
      
    def g5_func(self, x):
        y = 0.0
        for i in xrange(len(x)):
            y += (x[i] - 0.5)**2
        return y
      
      
    def g7_func(self, x):
        y = 0.0
        for i in xrange(len(x)):
            y += x[i]
        return (9.0/len(x)) * y
      
    def h7_func(self, g):
        fdim = len(self.f)
        y = 0.0
        for i in xrange(len(self.f) - 1):
            y += (self.f[i]/(1.0 + g)) * (1.0 + sin( 3 * pi * self.f[i]))
        return fdim - y
      
      
    """ 
    The chomosome: x_1, x_2, ........, x_M-1, x_M, .........., x_M+k
                              [------- Vector x_M -------]
              x[0], x[1], ... ,x[fdim-2], x[fdim-1], ... , x[fdim+k-1] 
    """
    
    def f1_obj_func(self, x):
        #print "in f1"
        x_M = []
        for i in xrange(len(self.f) - 1, len(x)):
            x_M.append(x[i])
        g = self.g_func(x_M)
      
        self.f[0] = 0.5 * (1.0 + g)
        for i in xrange(len(self.f) - 1):
            self.f[0] *= x[i]
          
        for i in xrange(1, len(self.f) - 1):
            self.f[i] = 0.5 * (1.0 + g)
            
            for j in xrange(len(self.f) - (i + 1)):
                self.f[i] *= x[j]
            self.f[i] *= 1 - x[len(self.f) - (i + 1)]
            
        self.f[len(self.f) - 1] = 0.5 * (1.0 - x[0]) * (1.0 + g)
        return self.f
        
      
    def f3_obj_func(self, x):
        #print "in f3"
        x_M = []
        for i in xrange(len(self.f) - 1, len(x)):
            x_M.append(x[i])
        g = self.g_func(x_M)
          
        self.f[0] = 1.0 + g
        for i in xrange(len(self.f) - 1):
            self.f[0] *= cos(x[i] * pi/2)
          
        for i in xrange(1, len(self.f) - 1):
            self.f[i] = 1.0 + g
            for j in xrange(len(self.f) - (i+1)):
                self.f[i] *= cos(x[j] * pi/2)
            self.f[i] *= sin(x[len(self.f) - (i+1)] * pi/2)
          
        self.f[len(self.f) - 1] = (1.0 + g) * sin(x[0]*pi/2)
        return self.f
        
      
    def f5_obj_func(self, x):
        #print "in f5"
        x_M = []
        for i in xrange(len(self.f) - 1, len(x)):
            x_M.append(x[i])
        g = self.g_func(x_M)
        
        theta = [0.0 for _ in xrange(len(self.f))]

        theta[0] = x[0]
        t = 1.0/(2.0 * (1.0 + g))
        
        for i in xrange(1, len(self.f)):
            theta[i] = t + ((g * x[i]) / (1.0 + g))
        
        self.f[0] = 1.0 + g
        for i in xrange(len(self.f) - 1):
            self.f[0] *= cos(theta[i] * pi/2)
          
        for i in xrange(1, len(self.f) - 1):
            self.f[i] = 1.0 + g
          
            for j in xrange(len(self.f) - (i+1)):
                self.f[i] *= cos(theta[j] * pi/2)
            self.f[i] *= sin(theta[len(self.f) - (i+1)] * pi/2)
          
        self.f[len(self.f) - 1] = (1.0 + g) * sin(theta[0]*pi/2)
        return self.f
        
    
    def f7_obj_func(self, x):
        #print "in f7"
        x_M = []
        for i in xrange(len(self.f) - 1, len(x)):
            x_M.append(x[i])
        g = 1.0 + self.g_func(x_M)
        
        for i in xrange(len(self.f) - 1):
            self.f[i] = x[i]
          
        self.f[len(self.f) - 1] = (1.0 + g) * self.h7_func(g)
        return self.f

"""
if __name__ == '__main__':
  print "Generic Experiments"
  dtlz_test = dtlz(40, 8, 7)
  min_obj, max_obj = dtlz_test.find_min_max()
  print dtlz_test.solution(min_obj, max_obj)
"""