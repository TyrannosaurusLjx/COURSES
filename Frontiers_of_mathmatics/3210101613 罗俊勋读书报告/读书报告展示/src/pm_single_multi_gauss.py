import numpy as np
import matplotlib.pyplot as plt

# 目标函数
def target_function(X):
    x, y = X
    epsilon = 0.1
    result = np.sin(np.pi * x / 3) * np.sin(np.pi * y / 3) + np.cos(np.pi * x / 4) * np.cos(np.pi * y / 4) + 2
    if np.abs(x) < epsilon and np.abs(y) < epsilon:
        return result + 1.5
    else:
        return result

# 初始化种群
def initialize_population(size, bounds, n_bits):
    return np.random.randint(2, size=(size, n_bits * len(bounds)))

# 解码二进制为实数
def decode_population(population, bounds, n_bits):
    decoded = []
    for individual in population:
        real_values = []
        for i, (low, high) in enumerate(bounds):
            binary_value = individual[i * n_bits:(i + 1) * n_bits]
            decimal_value = int("".join(map(str, binary_value)), 2)
            real_value = low + (high - low) * decimal_value / (2 ** n_bits - 1)
            real_values.append(real_value)
        decoded.append(real_values)
    return np.array(decoded)

# 计算适应度
def evaluate_population(population, bounds, n_bits):
    decoded_population = decode_population(population, bounds, n_bits)
    return np.array([target_function(ind) for ind in decoded_population])

# 选择
def select(population, fitness):
    probabilities = fitness / fitness.sum()
    indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[indices]

# 单点交叉
def crossover(parent1, parent2, crossover_rate):
    if np.random.rand() < crossover_rate:
        point = np.random.randint(1, len(parent1) - 1)
        child1 = np.concatenate((parent1[:point], parent2[point:]))
        child2 = np.concatenate((parent2[:point], parent1[point:]))
        return child1, child2
    return parent1, parent2

# 变异策略
def single_point_mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def multi_point_mutation(individual, mutation_rate, points=3):
    for _ in range(points):
        if np.random.rand() < mutation_rate:
            point = np.random.randint(len(individual))
            individual[point] = 1 - individual[point]
    return individual

def gaussian_mutation(individual, mutation_rate, bounds, n_bits):
    decoded = decode_population([individual], bounds, n_bits)[0]
    if np.random.rand() < mutation_rate:
        decoded += np.random.normal(0, 0.1, size=len(decoded))
        decoded = np.clip(decoded, [b[0] for b in bounds], [b[1] for b in bounds])
    return encode_individual(decoded, bounds, n_bits)

def encode_individual(decoded, bounds, n_bits):
    individual = []
    for value, (low, high) in zip(decoded, bounds):
        decimal = int((value - low) / (high - low) * (2 ** n_bits - 1))
        binary = list(map(int, bin(decimal)[2:].zfill(n_bits)))
        individual.extend(binary)
    return np.array(individual)

# 遗传算法
def genetic_algorithm(bounds, n_bits, n_generations, population_size, crossover_rate, mutation_rate, mutation_func, elite_size=1):
    population = initialize_population(population_size, bounds, n_bits)
    best_fitness_history = []
    best_fitness = float("-inf")
    best_individual = None

    for generation in range(n_generations):
        fitness = evaluate_population(population, bounds, n_bits)
        gen_best_index = np.argmax(fitness)
        gen_best_fitness = fitness[gen_best_index]
        gen_best_individual = population[gen_best_index]

        if gen_best_fitness > best_fitness:
            best_fitness = gen_best_fitness
            best_individual = gen_best_individual

        best_fitness_history.append(best_fitness)

        elite_individuals = population[np.argsort(fitness)[-elite_size:]]
        selected = select(population, fitness)
        next_generation = []

        for i in range(0, population_size - elite_size, 2):
            parent1, parent2 = selected[i], selected[i + 1]
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            next_generation.append(mutation_func(child1, mutation_rate))
            next_generation.append(mutation_func(child2, mutation_rate))

        next_generation = np.array(next_generation[:population_size - elite_size] + list(elite_individuals))
        population = next_generation

    return decode_population([best_individual], bounds, n_bits)[0], best_fitness, best_fitness_history


def main(n, iters):
    sigle = np.zeros(iters)
    multi = np.zeros(iters)
    gauss = np.zeros(iters)
    for i in range(n):
        # 比较三种变异策略
        bounds = [(-10, 10), (-10, 10)]
        n_bits = 16
        n_generations = iters
        population_size = 20
        crossover_rate = 0.8
        mutation_rate = 0.05

        strategies = {
            "Single-Point Mutation": single_point_mutation,
            "Multi-Point Mutation": lambda ind, rate: multi_point_mutation(ind, rate, points=3),
            "Gaussian Mutation": lambda ind, rate: gaussian_mutation(ind, rate, bounds, n_bits),
        }

        fitness_histories = {}
        for name, mutation_func in strategies.items():
            # print(f"Running with {name}...")
            _, best_fitness, fitness_history = genetic_algorithm(
                bounds, n_bits, n_generations, population_size, crossover_rate, mutation_rate, mutation_func
            )
            fitness_histories[name] = fitness_history
            if name == "Single-Point Mutation":
                sigle += np.array(fitness_history)
            elif name == "Multi-Point Mutation":
                multi += np.array(fitness_history)
            else:
                gauss += np.array(fitness_history)
    sigle = sigle / n
    multi = multi / n
    gauss = gauss / n
    ## 画出三种变异策略的折线图
    plt.figure(figsize=(10, 6))
    plt.plot(sigle, label="Single-Point Mutation")
    plt.plot(multi, label="Multi-Point Mutation")
    plt.plot(gauss, label="Gaussian Mutation")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Comparison of Mutation Strategies")
    plt.legend()
    plt.show()
    
main(20, 100)