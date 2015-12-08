from dtlz import Model, dtlz
population_size = 700

def baseline(model):
    base_min, base_max = model.find_min_max()
    return base_min, base_max

def basePopulation(model, base_min, base_max):
     #choose initial population
    """
    population <- initializePopulation(population_size, problem_size)
    """
    population = []
    for _ in xrange(population_size):
        candidate = model.solution(base_min, base_max)
        population.append(candidate)
        #print len(candidate)
    return population

def return_baseline():
	model = dtlz(10, 2, 1)
	return baseline(model)

def return_basepop(model, base_min, base_max):
	return basePopulation(model, base_min, base_max)
