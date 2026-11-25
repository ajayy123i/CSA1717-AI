import random

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [random.randint(0, 31) for i in range(6)]

# Genetic algorithm
for generation in range(20):

    population.sort(key=fitness, reverse=True)

    # Select best individuals
    parents = population[:3]

    # Create new population
    new_population = parents.copy()

    while len(new_population) < 6:
        p1, p2 = random.sample(parents, 2)

        # Crossover
        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.2:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

best = max(population, key=fitness)

print("Best solution:", best)
print("Maximum value:", fitness(best))
