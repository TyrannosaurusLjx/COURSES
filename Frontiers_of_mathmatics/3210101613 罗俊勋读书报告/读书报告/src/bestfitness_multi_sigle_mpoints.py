import numpy as np
import matplotlib.pyplot as plt

# 定义优化目标函数（假设目标是最大化此函数的值）
def fitness_function(x):
    return np.sin(x) + np.cos(5 * x) + 1 / (1 + 0.4 * x**2) + 3

# 初始化种群
def initialize_population(pop_size, genome_length):
    # 初始化为 [-10, 10] 范围内的随机数
    return np.random.uniform(-10, 10, (pop_size, genome_length))

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

# 多点变异操作
def multi_point_mutate(individual, mutation_prob, l=2):
    mutation_points = np.random.choice(len(individual), size=l, replace=False)
    for point in mutation_points:
        if np.random.rand() < mutation_prob:
            individual[point] += np.random.normal(0, 0.1)
    return individual

# 遗传算法主流程（多点变异）
def genetic_algorithm_multi_point(pop_size, genome_length, generations, pm=0.1, pc=0.9, l=2):
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
            next_generation.append(multi_point_mutate(child1, mutation_prob, l))
            next_generation.append(multi_point_mutate(child2, mutation_prob, l))
        
        population = np.array(next_generation)

    return best_fitness_over_time

# 参数设置
POP_SIZE = 100
GENOME_LENGTH = 40  # 假设基因长度为 30
GENERATIONS = 100
N = 200  # 执行次数
L = 7
Lst = [2, 3, 5, 7, 9, 11]

# 初始化结果存储
fitness_single_point = np.zeros(GENERATIONS)
fitness_multi_points = np.zeros((L, GENERATIONS))

# 执行单点变异和多点变异GA多次并计算平均适应度
for _ in range(N):
    fitness_single_point += genetic_algorithm_multi_point(POP_SIZE, GENOME_LENGTH, GENERATIONS, l=1)  # l=1表示每个个体变异1个基因点 
    k = 0
    for i in Lst:
        fitness_multi_points[k] += genetic_algorithm_multi_point(POP_SIZE, GENOME_LENGTH, GENERATIONS, l=i)
        k += 1

# 计算平均值
fitness_single_point /= N
fitness_multi_points /= N

# 绘制对比图
plt.plot(fitness_single_point, label="Single Point Mutation")
k = 0
for i in Lst:
    plt.plot(fitness_multi_points[k], label=f"Multi Point Mutation (points={i})")
    k += 1
plt.xlabel("Generation")
plt.ylabel("Best Fitness For Every Generation")
plt.legend()
plt.title("Comparison of Single and Multi Point Mutation in GA")
plt.savefig("../assets/img/ga_comparison_mutation.jpg")
plt.show()