from sk import rdivDemo
from model import dtlz7
from optimizers import simulatedAnnealing, maxWalkSat, differentialEvolution

def type3(data):
    rdivDemo(data)
    

for model in [dtlz7]:
    data = [['sa'],['mws'],['de']]
    for _ in range(20):
        for optimizer in [simulatedAnnealing, maxWalkSat, differentialEvolution]:
            #k = -1
            print "\n" * 5
            print "*****************************************"
            print "Model", model.__name__
            print "Optimizer", optimizer.__name__
            final_era, era_energy = optimizer(model)
        
            if optimizer.__name__ == "simulatedAnnealing":
                k = 0
            if optimizer.__name__ == "maxWalkSat":
                k = 1  
            if optimizer.__name__ == "differentialEvolution":
                k = 2 
            
            for each in final_era:
                data[k].append(each)
            print "*****************************************"
        
        #print data
#test = [[1,2,3],[4,5,6],[7,8,9]]
    type3(data)