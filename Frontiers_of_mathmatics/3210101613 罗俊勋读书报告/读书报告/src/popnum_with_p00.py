import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

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

# 遗传算法主流程（统计每代模式数量）
def genetic_algorithm(pop_size, genome_length, generations, p_00=0.5):
    population = initialize_population(pop_size, genome_length, p_00)
    schema_counts_over_time = []  # 存储每代的模式数量

    for gen in range(generations):
        # 统计模式数量
        schema_counts = Counter([ind[:2] for ind in population])
        schema_counts_over_time.append(schema_counts)

        # 计算适应度
        fitness = np.array([calculate_fitness(ind) for ind in population])

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

    return schema_counts_over_time

# 参数设置
POP_SIZE = 100
GENOME_LENGTH = 6
GENERATIONS = 30
RATIO = 0.5  # 初始 00 比例
N = 100 # 运行次数

for RATIO in [0.25, 0.40, 0.55, 0.70]:
    labels = ["11", "00", "01", "10"]
    counts00 = np.zeros(GENERATIONS)
    counts11 = np.zeros(GENERATIONS)
    counts01 = np.zeros(GENERATIONS)
    counts10 = np.zeros(GENERATIONS)

    for _ in range(N):
        # 运行遗传算法
        schema_counts_over_time = genetic_algorithm(POP_SIZE, GENOME_LENGTH, GENERATIONS, p_00=RATIO)

        # 累加每代的模式数量
        for gen, schema_counts in enumerate(schema_counts_over_time):
            counts00[gen] += schema_counts.get("00", 0)
            counts11[gen] += schema_counts.get("11", 0)
            counts01[gen] += schema_counts.get("01", 0)
            counts10[gen] += schema_counts.get("10", 0)

    # 计算平均值
    counts00 /= N
    counts11 /= N
    counts01 /= N
    counts10 /= N

    # 保存图片
    generations = np.arange(GENERATIONS)
    plt.figure(figsize=(10, 6))
    plt.plot(generations, counts00, label="00", color="blue")
    plt.plot(generations, counts11, label="11", color="red")
    plt.plot(generations, counts01, label="01", color="green")
    plt.plot(generations, counts10, label="10", color="orange")
    plt.xlabel("Generation")
    plt.ylabel("Average Count")
    plt.legend()
    plt.title(f"Schema Counts over Generations (p_00={RATIO})")
    plt.savefig(f"../assets/img/popnum_with_p00_{RATIO}.jpg")
    plt.close()

print("done")