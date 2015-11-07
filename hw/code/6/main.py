from models import Schaffer, Osyczka2, Kursawe
from optimizers import simulatedAnnealing, maxWalkSat 

for model in [Schaffer, Osyczka2, Kursawe]:
 for optimizer in [simulatedAnnealing, maxWalkSat]:
     print "\n" * 5
     print "*****************************************"
     print "Model", model.__name__
     print "Optimizer", optimizer.__name__
     optimizer(model)
     print "*****************************************"

#maxWalkSat(Schaffer)

