import math
from sk import rdivDemo
from model import dtlz7
from optimizers import simulatedAnnealing, maxWalkSat, differentialEvolution

final_era = [[ ], [ ], [ ]]
zero_era = [[ ], [ ], [ ]]
data = [['sa'],['mws'],['de']]

def type3(final_era, zero_era):
    i=0
    for final_opt, zero_opt in zip(final_era,zero_era):
        losses = [ ]
        length = min(len(final_opt), len(zero_opt))
        for each in range(length):
            final_cand = final_opt[each]
            zero_cand = zero_opt[each]
            num = (final_cand[1]-zero_cand[1])**2 + (final_cand[0]-zero_cand[0])**2
            den = 2
            rms_dist = math.sqrt(num/den)
            #print rms_dist
            losses.append(rms_dist)
        for each in losses:
            data[i].append(each)
        i=i+1
    #print data
            
    rdivDemo(data)
    

for model in [dtlz7]:
    for _ in range(20):
        for optimizer in [simulatedAnnealing, maxWalkSat, differentialEvolution]:
            print "\n" * 5
            print "*****************************************"
            print "Model", model.__name__
            print "Optimizer", optimizer.__name__
            each_final_era, each_zero_era = optimizer(model)
            #print "Final era" ,final_era
        
            if optimizer.__name__ == "simulatedAnnealing":
                k = 0
            if optimizer.__name__ == "maxWalkSat":
                k = 1  
            if optimizer.__name__ == "differentialEvolution":
                k = 2 
            
            for each in each_final_era:
                final_era[k].append(each)
            for each in each_zero_era:
                zero_era[k].append(each)
            print "*****************************************"
        
type3(final_era, zero_era)

#Hypervolume calculation
l = 0
for each_opt in final_era:
    if l==0:
        filename = './Pareto_Fronts/sa.txt'
    if l==1:
        filename = './Pareto_Fronts/mws.txt'
    if l==2:
        filename = './Pareto_Fronts/de.txt'
    f = open(filename, 'w')
    for each in each_opt:
        print >> f, each[0], each[1]
    f.close()
    l=l+1


    
    

