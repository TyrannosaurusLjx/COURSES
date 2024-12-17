import numpy as np
import matplotlib.pyplot as plt

# 定义优化目标函数（假设目标是最大化此函数的值）
def fitness_function(x):
    return np.sin(x) + np.cos(5 * x) + 1 / (1 + 0.4 * x**2) + 3

# 初始化种群
def initialize_population(pop_size, genome_length):
    # 初始化为 [-10, 10] 范围内的随机数
    return np.random.uniform(-10, 10, (pop_size, genome_length))

# 带GW的初始化
def initialize_population_with_gw(pop_size, genome_length, gw_length):
    active_part = initialize_population(pop_size, genome_length - gw_length)
    gw_part = np.random.uniform(0, 1, (pop_size, gw_length))  # 交叉和变异概率
    return np.hstack((active_part, gw_part))

# 解码遗传废料（GW）
def decode_gw(individual, genome_length, gw_length):
    active_part = individual[:genome_length - gw_length]
    crossover_prob = individual[genome_length - gw_length]
    mutation_prob = individual[genome_length - gw_length + 1]
    return active_part, crossover_prob, mutation_prob

# 适应度计算
def calculate_fitness(population):
    return np.array([np.mean(fitness_function(ind)) for ind in population])

# 选择操作（轮盘赌选择）
def select_mating_pool(population, fitness, num_mates):
    prob = fitness / fitness.sum()
    indices = np.random.choice(len(population), size=num_mates, p=prob)
    return population[indices]

# 交叉操作
def crossover(parent1, parent2, crossover_prob):
    if np.random.rand() < crossover_prob:
        point = np.random.randint(1, len(parent1) - 1)
        child1 = np.hstack((parent1[:point], parent2[point:]))
        child2 = np.hstack((parent2[:point], parent1[point:]))
        return child1, child2
    return parent1, parent2

# 变异操作
def mutate(individual, mutation_prob):
    for i in range(len(individual)):
        if np.random.rand() < mutation_prob:
            individual[i] += np.random.normal(0, 0.1)
    return individual

# 遗传算法主流程（带无义密码子GW）
def genetic_algorithm_with_gw(pop_size, genome_length, generations, gw_length=2, pm=0.1, pc=0.9):
    population = initialize_population_with_gw(pop_size, genome_length, gw_length)
    best_fitness_over_time = []

    for gen in range(generations):
        fitness = calculate_fitness(population)
        best_fitness_over_time.append(np.max(fitness))

        # 选择父代
        mating_pool = select_mating_pool(population, fitness, pop_size // 2)

        # 生成下一代
        next_generation = []
        for i in range(0, len(mating_pool), 2):
            p1, p2 = mating_pool[i], mating_pool[(i + 1) % len(mating_pool)]
            
            # 解码GW部分（交叉和变异概率）
            _, crossover_prob1, mutation_prob1 = decode_gw(p1, genome_length, gw_length)
            _, crossover_prob2, mutation_prob2 = decode_gw(p2, genome_length, gw_length)
            
            crossover_prob = (crossover_prob1 + crossover_prob2) / 2
            mutation_prob = (mutation_prob1 + mutation_prob2) / 2

            # 执行交叉与变异操作
            child1, child2 = crossover(p1, p2, crossover_prob)
            next_generation.append(mutate(child1, mutation_prob))
            next_generation.append(mutate(child2, mutation_prob))
        
        population = np.array(next_generation)

    return best_fitness_over_time

# 遗传算法主流程（不带无义密码子GW）
def genetic_algorithm_without_gw(pop_size, genome_length, generations, pm=0.1, pc=0.9):
    population = initialize_population(pop_size, genome_length)
    best_fitness_over_time = []

    for gen in range(generations):
        fitness = calculate_fitness(population)
        best_fitness_over_time.append(np.max(fitness))

        # 选择父代
        mating_pool = select_mating_pool(population, fitness, pop_size // 2)

        # 生成下一代
        next_generation = []
        for i in range(0, len(mating_pool), 2):
            p1, p2 = mating_pool[i], mating_pool[(i + 1) % len(mating_pool)]
            
            # 固定的交叉和变异概率
            crossover_prob = pc
            mutation_prob = pm

            # 执行交叉与变异操作
            child1, child2 = crossover(p1, p2, crossover_prob)
            next_generation.append(mutate(child1, mutation_prob))
            next_generation.append(mutate(child2, mutation_prob))
        
        population = np.array(next_generation)

    return best_fitness_over_time

# 参数设置
POP_SIZE = 100
GENOME_LENGTH = 40  # 假设基因长度为 20
GW_LENGTH = 2  # 无义密码子部分为 2
GENERATIONS = 300
N = 40  # 执行次数

# 初始化结果存储
fitness_standard = np.zeros(GENERATIONS)
fitness_with_gw = np.zeros(GENERATIONS)

# 执行标准GA和带GW的GA多次并计算平均适应度
for _ in range(N):
    fitness_standard += genetic_algorithm_without_gw(POP_SIZE, GENOME_LENGTH, GENERATIONS)
    fitness_with_gw += genetic_algorithm_with_gw(POP_SIZE, GENOME_LENGTH, GENERATIONS, GW_LENGTH)

# 计算平均值
fitness_standard /= N
fitness_with_gw /= N

# 绘制对比图
plt.plot(fitness_standard, label="Standard GA")
plt.plot(fitness_with_gw, label="GA with Genetic Waste (GW)")
plt.xlabel("Generation")
plt.ylabel("Best Fitness For Every Generation")
plt.legend()
plt.title("Comparison of GA Performance with and without Genetic Waste (GW)")
plt.savefig("../assets/img/comparison_gw_vs_standard.jpg")
plt.show()