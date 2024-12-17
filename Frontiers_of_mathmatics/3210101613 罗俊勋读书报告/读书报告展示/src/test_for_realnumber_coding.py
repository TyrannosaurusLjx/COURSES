import numpy as np
from scipy.stats import norm
from math import modf
import matplotlib.pyplot as plt

## @class GA
#  @brief 遗传算法类，用于求解优化问题。
class GA:
    ## @brief 初始化遗传算法。
    #  @param pc 交叉概率，值需在 [0, 1] 之间。
    #  @param pm 变异概率，值需在 [0, 1] 之间。
    #  @param pop_size 种群大小，必须为正整数。
    #  @param dimension 自变量的维度个数。
    #  @param head_size 每个变量整数部分的位数。
    #  @param tail_size 每个变量小数部分的位数。
    #  @param target_func 目标函数，用于计算适应度。
    def __init__(self,
                 pc: float,
                 pm: float,
                 pop_size: int,
                 dimension: int,
                 head_size: np.ndarray,
                 tail_size: np.ndarray,
                 target_func: callable): # type: ignore
        self.pc = pc
        self.pm = pm
        self.pop_size = pop_size
        self.n = dimension
        self.head_size = head_size
        self.tail_size = tail_size
        self.target_func = target_func
        self.best_chromosome = ''
        self.chromosome_size = np.sum(self.head_size) + np.sum(self.tail_size) + self.n
        self.evolve_path = []

    ## @brief 将实数编码为染色体字符串。
    #  @param X 输入的实数数组。
    #  @return 编码后的染色体字符串。
    def encoding(self, X: np.ndarray) -> str:
        chromosomes = ''
        for i in range(self.n):
            x = X[i]
            _, head = modf(abs(x))
            head_str = str(int(head)).zfill(self.head_size[i])
            tail_str = str(x).split('.')[1].zfill(self.tail_size[i])[:self.tail_size[i]]
            chromosome = head_str + tail_str
            chromosome = ('1' if x < 0 else '0') + chromosome
            chromosomes += chromosome
        return chromosomes
    
    ## @brief 将染色体字符串解码为实数数组。
    #  @param chromosomes 输入的染色体字符串。
    #  @return 解码后的实数数组。
    def decoding(self, chromosomes: str) -> np.ndarray:
        if len(chromosomes) != self.chromosome_size:
            raise ValueError(f"Expected length: {self.chromosome_size}, Actual length: {len(chromosomes)}")
        X = np.zeros(self.n)
        index = 0
        for i in range(self.n):
            chromosome = chromosomes[index:index + self.head_size[i] + self.tail_size[i] + 1]
            index += self.head_size[i] + self.tail_size[i] + 1
            head = int(chromosome[1:1 + self.head_size[i]])
            tail = float(int(chromosome[1 + self.head_size[i]:]) / 10 ** self.tail_size[i])
            x = head + tail
            X[i] = x if chromosome[0] == '0' else -x
        return X
    
    ## @brief 初始化种群。
    def init_population(self):
        def get_x_by_size(head_size: int) -> float:
            x = np.random.uniform(-10 * head_size, 10 * head_size)
            return x
        self.population = np.array([self.encoding(np.array([get_x_by_size(head_size) for head_size in self.head_size])) for _ in range(self.pop_size)])
        self.best_chromosome = self.population[0]
        return self.population

    ## @brief 适应度函数，使用 sigmoid 归一化目标函数值。
    #  @param X 输入的实数数组。
    #  @return 适应度值。
    def fitness(self, X: np.ndarray) -> float:
        value = self.target_func(X)
        # value = np.clip(value, -100, 100)
        # return 1 / (1 + np.exp(-value))
        return value
        
    ## @brief 选择操作，使用轮盘赌法选择个体。
    def choose(self) -> None:
        fitness = np.array([self.fitness(self.decoding(chromosome)) for chromosome in self.population])
        probabilities = fitness / np.sum(fitness)
        best_index = np.argmax(fitness)
        self.best_chromosome = max(self.best_chromosome, self.population[best_index], key=lambda c: self.fitness(self.decoding(c)))
        self.population = np.random.choice(self.population, size=self.pop_size, p=probabilities)

    ## @brief 交叉操作，随机选择交叉点进行基因重组。
    def crossover(self):
        for i in range(len(self.population) - 1):
            point = len(self.population[i]) // 2
            next_index = (i + 1) % len(self.population)
            offspring1 = self.population[i][:point] + self.population[next_index][point:]
            offspring2 = self.population[next_index][:point] + self.population[i][point:]
            # Replace the original individuals
            self.population[i] = offspring1
            self.population[next_index] = offspring2   
    ## @brief 变异操作，单点变异。
    def mutate(self) -> None:
        for i in range(self.pop_size):
            if np.random.rand() < self.pm:
                point = np.random.randint(0, self.chromosome_size)
                local_chromosome = list(self.population[i])
                local_chromosome[point] = str(np.random.randint(0, 10))
                self.population[i] = ''.join(local_chromosome)
    
    ## @brief 进行一代的选择、交叉和变异。
    def evolve(self) -> None:
        self.choose()
        self.crossover()
        self.mutate()
    
    ## @brief 运行遗传算法。
    #  @param generations 进化的代数。
    def run(self, generations: int) -> None:
        self.init_population()
        for i in range(generations):
            self.evolve()
            self.evolve_path.append(self.fitness(self.decoding(self.best_chromosome)))
            self.population[0] = self.best_chromosome
    
    def plot_evolve_path(self):
        import matplotlib.pyplot as plt
        plt.plot(self.evolve_path)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Evolve Path')
        plt.show()
    
    ## @brief 获取当前种群中的最优解。
    #  @return 最优解对应的实数数组。
    def get_best(self) -> np.ndarray:
        return self.decoding(self.best_chromosome)
    
    def get_best_in_pop(self) -> np.ndarray:
        best_chromosome = max(self.population, key=lambda c: self.fitness(self.decoding(c)))
        return self.decoding(best_chromosome)

def target_function(X: np.ndarray) -> float:
    x, y = X
    epsilon = 0.1
    result = np.sin(np.pi*x / 3)*np.sin(np.pi*y / 3) + np.cos(np.pi*x / 4)*np.cos(np.pi*y/ 4) + 2
    if np.abs(x) < epsilon and np.abs(y) < epsilon:
        return result + 1.5
    else:
        return result
    
def plot(target_func: callable):
    X = np.linspace(-10, 10, 200)
    Y = np.linspace(-10, 10, 200)
    Z = np.array([[target_func(np.array([x, y])) for x in X] for y in Y])
    X, Y = np.meshgrid(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.show()
    
def main():
    times = 1000
    pc = 1
    pm = 0.05
    pop_size = 600
    dimension = 2
    head_size = np.array([1, 1])
    tail_size = np.array([2, 2])
    ga = GA(pc, pm, pop_size, dimension, head_size, tail_size, target_function)
    result = []
    for i in range(times):
        ga.run(200)
        X = ga.get_best()
        # print("Final Result: Best Fitness = {}, x = {}, y = {}".format(target_function(X), X[0], X[1]))
        result.append(target_function(X))
    result = np.array(result)
    count = np.count_nonzero(result[result > 4])
    ratio = count / times
    print(f'count: {count}, ratio: {ratio}')
# main()
#count: 641, ratio: 0.641