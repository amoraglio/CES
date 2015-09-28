#
# Convex Search Algorithm
#

import random

### POPULATION LEVEL ###

def convex_search():
    population = create_pop()
    fitness_population = evaluate_pop(population)
    print min(fitness_population)
    while not all_equal(population): # check converged population
        if not all_equal(fitness_population):
            mating_pool = select_better_than_worst(population, fitness_population)
        else:
            mating_pool = population
        #print mating_pool
        population = convex_recombination_pop(mating_pool)
        fitness_population = evaluate_pop(population)
        print min(fitness_population)
    return (population[0], fitness_population[0]) #return first individual

### INDIVIDUAL LEVEL ###

def create_pop():
    return [ create_ind() for _ in range(POPULATION_SIZE) ]

def evaluate_pop(population):
    return [ evaluate_ind(individual) for individual in population ]

def all_equal(bunch):
    return all(x==bunch[0] for x in bunch)

def select_better_than_worst(population, fitness_population):
    worst_fitness = min(fitness_population)
    return [ individual for (individual, fitness) in zip(population, fitness_population) if fitness > worst_fitness ]

def convex_recombination_pop(mating_pool):
    return [ convex_recombination_ind(mating_pool) for _ in range(POPULATION_SIZE) ]

### REPRESENTATION LEVEL ###

def create_ind():
    return [ random.randint(0, 1) for _ in range(INDIVIDUAL_SIZE) ]

def evaluate_ind(individual): #leading_ones
    for position in range(INDIVIDUAL_SIZE):
        if individual[position] == 0:
            break
    else:
        position += 1
    return position

def convex_recombination_ind(mating_pool):
    transposed_mating_pool=zip(*mating_pool)
    def recombine_column(col):
        return col[0] if all_equal(col) else random.randint(0, 1)
    return map(recombine_column, transposed_mating_pool)

### EXPERIMENTS ###

POPULATION_SIZE = 25
INDIVIDUAL_SIZE = 10

print convex_search()
