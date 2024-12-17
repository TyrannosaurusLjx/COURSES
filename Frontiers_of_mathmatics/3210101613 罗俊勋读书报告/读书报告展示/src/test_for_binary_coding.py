import numpy as np

# 目标函数
def target_function(X: np.ndarray) -> float:
    x, y = X
    epsilon = 0.1
    result = np.sin(np.pi * x / 3) * np.sin(np.pi * y / 3) + np.cos(np.pi * x / 4) * np.cos(np.pi * y / 4) + 2
    if np.abs(x) < epsilon and np.abs(y) < epsilon:
        return result + 1.5
    else:
        return result

# 将二进制编码解码为实数
def decode(binary: np.ndarray, bounds: tuple, precision: int) -> float:
    decimal = int("".join(map(str, binary)), 2)
    min_bound, max_bound = bounds
    return min_bound + (max_bound - min_bound) * decimal / (2**precision - 1)

# 初始化种群
def initialize_population(pop_size, chrom_length):
    return np.random.randint(0, 2, (pop_size, chrom_length * 2))

# 计算种群的适应度
def evaluate_population(population, bounds, precision):
    fitness = []
    for individual in population:
        chrom_x, chrom_y = np.split(individual, 2)
        x = decode(chrom_x, bounds, precision)
        y = decode(chrom_y, bounds, precision)
        fitness.append(target_function([x, y]))
    return np.array(fitness)

# 选择操作（轮盘赌选择）
def select(population, fitness):
    probabilities = fitness / fitness.sum()
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[selected_indices]

# 单点交叉
def crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return child1, child2

# 单点变异
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]  # 翻转位
    return individual

# 遗传算法主程序
def genetic_algorithm(target_function, bounds, pop_size=100, chrom_length=10, generations=100, mutation_rate=0.01):
    # 初始化种群
    population = initialize_population(pop_size, chrom_length)

    # 主迭代
    for generation in range(generations):
        # 计算适应度
        fitness = evaluate_population(population, bounds, chrom_length)

        # 输出当前代最优解
        best_fitness = fitness.max()
        best_individual = population[fitness.argmax()]
        best_x = decode(best_individual[:chrom_length], bounds, chrom_length)
        best_y = decode(best_individual[chrom_length:], bounds, chrom_length)
        # print(f"Generation {generation}: Best Fitness = {best_fitness:.4f}, x = {best_x:.4f}, y = {best_y:.4f}")

        # 选择
        selected_population = select(population, fitness)

        # 交叉
        new_population = []
        for i in range(0, len(selected_population), 2):
            parent1, parent2 = selected_population[i], selected_population[(i + 1) % len(selected_population)]
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])
        population = np.array(new_population)

        # 变异
        population = np.array([mutate(individual, mutation_rate) for individual in population])

    # 返回最终最优解
    final_fitness = evaluate_population(population, bounds, chrom_length)
    best_fitness = final_fitness.max()
    best_individual = population[final_fitness.argmax()]
    best_x = decode(best_individual[:chrom_length], bounds, chrom_length)
    best_y = decode(best_individual[chrom_length:], bounds, chrom_length)
    return best_fitness, best_x, best_y

# 参数设置
bounds = (-10, 10)  
pop_size = 600      
chrom_length = 10   
generations = 200   
mutation_rate = 0.05  

# 运行遗传算法
count = 0
for i in range(1000):
    best_fitness, best_x, best_y = genetic_algorithm(target_function, bounds, pop_size, chrom_length, generations, mutation_rate)
    print(f"Final Result: Best Fitness = {best_fitness:.4f}, x = {best_x:.4f}, y = {best_y:.4f}")
    count += 1 if best_fitness > 4 else 0
print(f"Count: {count}, Ratio: {count / 1000}")
## Count: 76, Ratio: 0.076