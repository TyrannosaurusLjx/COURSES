import numpy as np
import matplotlib.pyplot as plt

# 定义适应度表
fitness_table = {
    "11": 1.1,
    "00": 1.0,
    "01": 0.9,
    "10": 0.5
}

# 适应度计算
def calculate_fitness(individual):
    key = individual[:2]  # 取前两位决定类别
    return fitness_table[key]

# 初始化种群
def initialize_population(pop_size, genome_length, p_00=0.5):
    population = []
    for _ in range(pop_size):
        if np.random.rand() < p_00:  # 控制 00 的比例
            individual = "00" + "".join(np.random.choice(["0", "1"], genome_length - 2))
        else:
            individual = "".join(np.random.choice(["0", "1"], genome_length))
        population.append(individual)
    return np.array(population)

# 选择操作（轮盘赌法）
def select_mating_pool(population, fitness, num_mates):
    prob = fitness / fitness.sum()
    indices = np.random.choice(len(population), size=num_mates, p=prob)
    return population[indices]

# 交叉操作
def crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1))  # 随机交叉点
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# 变异操作
def mutate(individual, mutation_rate=0.01):
    mutated = list(individual)
    for i in range(len(mutated)):
        if np.random.rand() < mutation_rate:
            mutated[i] = "1" if mutated[i] == "0" else "0"
    return "".join(mutated)

# 遗传算法主流程
def genetic_algorithm(pop_size, genome_length, generations, p_00=0.5):
    population = initialize_population(pop_size, genome_length, p_00)
    best_fitness_over_time = []

    for gen in range(generations):
        fitness = np.array([calculate_fitness(ind) for ind in population])
        best_fitness_over_time.append(np.max(fitness))

        # 选择父代
        mating_pool = select_mating_pool(population, fitness, pop_size // 2)

        # 生成下一代
        next_generation = []
        for i in range(0, len(mating_pool), 2):
            p1, p2 = mating_pool[i], mating_pool[(i+1) % len(mating_pool)]
            child1, child2 = crossover(p1, p2)
            next_generation.append(mutate(child1))
            next_generation.append(mutate(child2))

        population = np.array(next_generation)

    return best_fitness_over_time

# 参数设置
POP_SIZE = 20
GENOME_LENGTH = 6
GENERATIONS = 20

# 测试不同初始 00 比例
ratios = [0.2, 0.5, 0.8, 1.0]
results = {ratio: np.zeros(GENERATIONS) for ratio in ratios}
for i in range(100):
    for ratio in ratios:
        results[ratio] += genetic_algorithm(POP_SIZE, GENOME_LENGTH, GENERATIONS, p_00=ratio)

# 绘制结果
for ratio, fitness in results.items():
    plt.plot(fitness, label=f"p_00={ratio}")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Impact of Initial Ratio of '00' on GA Performance")
plt.legend()
plt.show()