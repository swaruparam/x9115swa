##A Simple Standard Genetic Algorithm

#### x9115swa - CSC 791 Respository
#####Contributers -
    sgandhi3@ncsu.edu
    sramakr6@ncsu.edu
    
**Instructions**

    1. Navigate to code/hw/9
    2. run "python ga.py"
    
###Abstract
_Genetic Algorithm is often used for solving optimization problems, it uses a natural selection process that mimics biological_
_evolution. This coding project implements genetic alorithm on DTLZ 1, 3, 5, and 7 models. To visualize how genetic algorithm_
_works, we first implement GA on DTLZ 1 with 500 decisions and 3 objectives. This is followed by the implementation on DTLZ 1, 3, 5_
_and 7 with 2, 4, 6,8 objectives and 10, 20, 40 decisions. We use "From Hell" distance, and hypervolume metrics to quantify the_
_improvement in population in the objective space._
    
###Objective
The objective of this project is to understand and compare the performance of GA on four variants of the DTLZ model. This is done by implementing GA with the default parameters for probability of mutation, crossover, select, number of candidates and number of generations. The report is divided into five sections, starting with the description of genetic algorithm, its implementation, followed by results, threat to validity and future work.

###Genetic Algorithm
Genetic Algorithm starts by initializing a population with fixed number of candidates, from that population it selects two parents by a select method e.g. binary domination, roulette wheel etc.. It then swaps the parent candidates, a process also known as crossover, followed by mutating the children generated as the result of crossover. If the generated children is fitter than the previous population candidates, it appends it to the population. To decide which candidates go into the next generation, all the candidates in the resulting population are sorted based on their scores, and any x% of best candidates are retained. We can also add a few unfit candidates to the next generation to maintain the diversity of the population. This generation is then used as a base population to select parents, and the whole process is repeated till the population converges and terminates early or till the maximum number of generations are reached.
    
###Implementation
The implementation of the genetic algorithm is based on the pseudo code mentioned in [1]. With the following modifications -

1. All the parameters are set to the values as given in the project specification.
2. *Type 1 comparison* is used twice, first for selection of parent population for which we employ binary domination, and second for selction of fitter child after mutation, here we employ continuous domination. The methods are implemented as in [2]
3. *Type 2 comparison* is used for early termination, and is implented using Krall's BStop method, and checked every 100 generations.
4. One point crossover is used to implement the crossover method.
5. *Pruning* is done every generation, where we retain 90% good candidates, and 10% bad candidates. In every generation the resultant population is sorted using CDOM, and then 90% candidates from the best end and 10% candidates from the bad end are kept in i+1th generation.

To visualize the working of GA on DTLZ we first implemented it on DTLZ 1 with 10 decisions, and 3 objectives for 500 candidates and 100 generations. Though we were not able to see the proper frontier, we did see the solutions getting converge in the objective space. The visualizations can be seen below - 

--------------------------------------------------------------------------------------------------------------------------------------

**DTLZ 1 - _Baseline Era_ and _Final Era_**

<img src = "https://cloud.githubusercontent.com/assets/7557398/11612920/8ff35c08-9bdb-11e5-8cf1-93882a67f9d9.png" width = "420" height="320"> <img src = "https://cloud.githubusercontent.com/assets/7557398/11612925/9008310a-9bdb-11e5-9969-826b12de8dea.png" width = "420" height="320">

**DTLZ 3 - _Baseline Era_ and _Final Era_**

<img src = "https://cloud.githubusercontent.com/assets/7557398/11612919/8ff20088-9bdb-11e5-9efb-6ba07593337c.png" width = "420" height="320"> <img src = "https://cloud.githubusercontent.com/assets/7557398/11612921/8ff79fb6-9bdb-11e5-8c69-833b18f40060.png" width = "420" height="320">

**DTLZ 5 - _Baseline Era_ and _Final Era_**

<img src = "https://cloud.githubusercontent.com/assets/7557398/11612922/8ff7c55e-9bdb-11e5-83f4-444601268bb0.png" width = "420" height="320"> <img src = "https://cloud.githubusercontent.com/assets/7557398/11612923/8ffbdcca-9bdb-11e5-9bdb-b43a4367cf21.png" width = "420" height="320">

**DTLZ 7 - _Baseline Era_ and _Final Era_**

<img src = "https://cloud.githubusercontent.com/assets/7557398/11612924/8ffd14e6-9bdb-11e5-8fae-f141f34521c7.png" width = "420" height="320"> <img src = "https://cloud.githubusercontent.com/assets/7557398/11612918/8ff0e478-9bdb-11e5-9a9a-6c2b86ff3200.png" width = "420" height="320">

--------------------------------------------------------------------------------------------------------------------------------------

###Results
Divergence and Hypervolume are used to evaluate the performance of GA on DTLZ 1, 3, 5 and 7. 

**Divergence**

To quantify the change in the frontier from the baseline population, we used the **from Hell** calculation. For each candidate on the final frontier, the nearest candidate on baseline was found using the nearest neighbour algorithm. The euclidean distance used to find the corresponding closest baseline candidate for each final frontier frontier candidate, was then averaged over the entire population and gave us the divergence of the frontier from the baseline, which we have assumed to be the **point of hell* for our final frontier.

![2and4_1](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/1.png?raw=true)
![2and4_2](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/2.png?raw=true)
![2and4_3](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/3.png?raw=true)
![2and4_4](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/4.png?raw=true)

![6and8_1](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/1%20(1).png?raw=true)
![6and8_2](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/2%20(1).png?raw=true)
![6and8_3](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/3%20(1).png?raw=true)
![6and8_4](https://github.com/shgandhi/s9115hga/blob/master/hw/code/9/img/Divergence%20Snapshots/4%20(1).png?raw=true)

--------------------------------------------------------------------------------------------------------------------------------------

**Hypervolume calculation**
Hypervolume is calculated using the code provided at [3]. 

![Hypervolume](https://cloud.githubusercontent.com/assets/7557398/11613520/e42962d4-9bf1-11e5-827d-38cf49876b0a.JPG)
--------------------------------------------------------------------------------------------------------------------------------------

###Threats to Validity
1. Since divergence used to compare the performance of GA is actually the euclidean distance from the baseline population, we have assumed that the population moves closer to heaven (away from the baseline), but we had no method of determing the direction in which  population moves, as the euclidean distance is always positive.
2. The percentage of good and bad candidates retained at the end of every generation is determined by magic numbers selected by hit and trial, and could have influenced the final result.

###Future Work
1. This work is extended in Code 10 and the magic numbers used for the parameters in the code are decided using DE. This can be done with other algorithms as well to see a more comprehensive comparison.
2. The same problem could be optimized using NSGA II, SPEA and GALE, and we can see then where does GA stand in this comparison.

###References
1. [Clever Algorithms - GA pseudo code](http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html)
2. [Less Than](https://github.com/txt/mase/blob/master/lessthan.md)
3. [Hypervolume Code](https://github.com/ai-se/Spread-HyperVolume)
