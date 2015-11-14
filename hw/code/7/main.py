from models import Schaffer, Osyczka2, Kursawe, Golinski
from optimizers import simulatedAnnealing, maxWalkSat, differentialEvolution

for model in [Schaffer, Osyczka2, Kursawe,Golinski]:
 for optimizer in [simulatedAnnealing, maxWalkSat, differentialEvolution]:
     print "\n" * 5
     print "*****************************************"
     print "Model", model.__name__
     print "Optimizer", optimizer.__name__
     optimizer(model)
     print "*****************************************"


