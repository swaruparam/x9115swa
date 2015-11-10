import random
import math

# generic model class
class Model(object):
    def __init__(self):
        self.no_decs = 0
        self.no_objs = 0
        self.decs = [ ]
        self.min_range = [ ]
        self.max_range = [ ]
        
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
        
    def eval_can(self):
        return [ ]
        
    def can_energy(self):
        return sum(self.eval_can())
        
    def baseline_study(self): #to find min and max energies
        energies = [ ]
        for _ in range(1000):
            self.any_can()
            energies.append(sum(self.eval_can()))
        return [min(energies), max(energies)]
    
    
class Schaffer (Model):
    def __init__(self):
        self.no_decs = 1
        self.no_objs = 2
        self.decs = [0]
        self.min_range = [-100]
        self.max_range = [100]
        self.any_can()
        
    def f1(self):
        x = self.decs[0]
        return x**2

    def f2(self):
        x = self.decs[0]
        return (x-2)**2
            
    def eval_can(self):
        return [self.f1(), self.f2()]
        

class Osyczka2 (Model):
    def __init__(self):
        self.no_decs = 6
        self.no_objs = 2
        self.decs = [0, 0, 0, 0, 0, 0]
        self.min_range = [0, 0, 1, 0, 1, 0]
        self.max_range = [10, 10, 5, 6, 5, 10]    
        self.any_can()
        
    def ok(self):
        x = self.decs[:]
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
  
    def f1(self):
        x = self.decs[:]
        f = -(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)**2)*((x[3]-4)**2) + (x[4]-1)**2)
        return f

    def f2(self):
        x = self.decs[:]
        f2 = sum(xi**2 for xi in x)
        return f2
        
    def eval_can(self):
        return [self.f1(), self.f2()]
        
    
class Kursawe (Model):
    def __init__(self):
        self.no_decs = 3
        self.no_objs = 2
        self.decs = [0, 0, 0]
        self.min_range = [-5, -5, -5]
        self.max_range = [5, 5, 5]    
        self.any_can()   
        
    def f1(self):
        f = 0
        for i in range(self.no_decs-1):
            f = f + (-10)*math.exp((-0.2)*math.sqrt(self.decs[i]**2+self.decs[i+1]**2))
        return f
        
    def f2(self):
        f = 0
        a = 0.8
        b = 1.0
        for i in range(self.no_decs):
            f += math.pow(abs(self.decs[i]),a) + 5*math.sin(math.pow(self.decs[i],b))
        return f
    
    def eval_can(self):
        return [self.f1(), self.f2()]
        
class Golinski (Model):
    def __init__(self):
        self.no_decs = 7
        self.no_objs = 2
        self.decs = [0, 0, 0, 0, 0, 0, 0]
        self.min_range = [2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5.0]
        self.max_range = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]    
        self.any_can()    
        
    def ok(self):
        x = self.decs[:]
        #g1
        if (1.0/(x[0] * x[1]**2 * x[2])) - (1.0/27.0) > 0:
            return False
        #g2 - same as g1
        #g3
        if math.pow(x[3],3) / (x[1] * x[2]**2 * x[5]**4) - (1.0/1.93) > 0:
            return False
        #g4
        if math.pow(x[4],3) / (x[1] * x[2] * x[6]**4) - (1.0/1.93) > 0:
            return False
        #g5
        if (x[1] * x[2]) - 40 > 0:
            return False
        #g6
        if (x[0] / x[1]) - 12 > 0:
            return False
        #g7 
        if 5 - (x[0] / x[1]) > 0:
            return False
        #g8
        if 1.9 - x[3] + (1.5*x[5]) > 0:
            return False
        #g9
        if 1.9 - x[4] + (1.1*x[6]) > 0:
            return False
        #g10
        if self.f2() > 1300:
            return False
        
        a = (745.0*x[4]) / (x[1]*x[2])
        b = 1.575 * math.pow(10,8)
        
        #g11
        if math.sqrt(math.pow(a,2) + b) / (0.1 * math.pow(x[6],3)) > 1100:
            return False
        return True
            
        
    def f1(self):
        x = self.decs[:]
        
        fa_c = 0.785*x[0]*(x[1]**2)
        fa = fa_c*(10*(x[2]**2)/3 + 14.933*x[2] - 43.0934)
        
        fb_c = (-1.508)*x[0]
        fb = fb_c*((x[5]**2) + (x[6]**2))
        
        fc_c = 7.477
        fc = fc_c*((x[5]**3) + (x[6]**3))
        
        fd_c = 0.7854
        fd = fd_c*((x[3]*(x[5]**2)) + (x[4]*(x[6]**2)))
        
        f = fa+fb+fc+fd
        return f
        
    def f2(self):
        x = self.decs[:]
        num = math.sqrt(math.pow((745.0*x[3])/(x[1]*x[2]),2) + 1.69*pow(10,7)) 
        den = 0.1*math.pow(x[5],3)
        f = num / den
        return f
        
    def eval_can(self):
        return [self.f1(), self.f2()]