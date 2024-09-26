from typing import Callable, List, Tuple
import numpy as np
import matplotlib.pyplot as plt

## 定义目标函数
def target(x, y):
    return np.log(100 - x**2 - y**2)


## 求解 [x1,x2]\times [y1,y2] 上函数 f 的最大值

class SGA():
    def __init__(self) -> None:
        self.pc = 0.6 # 交叉概率
        self.pm = 0.01 # 变异概率
        self.M = 100 # 种群规模 (选择4 的倍数)
        self.l = 10 # 编码长度
        self.T = 1000 # 迭代次数
        self.target = lambda x: x # 目标函数
        self.f = lambda x: x # 适应度函数
        self.population = np.array([" " for _ in range(self.M)]) # 种群
        self.encode = lambda x: x # 编码函数
        self.decode = lambda x: x # 解码函数
        self.ranges = [0,1,0,1] # 变量范围

    def set_params(self, target: Callable, pc: float = 0.6, pm: float = 0.01, M: int = 100, T: int = 1000, f: Callable = None, encode: Callable = None, decode: Callable = None, ranges: List[float] = None) -> None:
        self.target = target
        self.pc = pc
        self.pm = pm
        self.M = M
        self.T = T
        self.f = f if f else self.f
        self.encode = encode if encode else self.encode
        self.decode = decode if decode else self.decode
        self.ranges = ranges if ranges else self.ranges

    def generate(self) -> List[float]:
        return [np.random.uniform(self.ranges[0], self.ranges[1]), np.random.uniform(self.ranges[2], self.ranges[3])]

    def init_population(self) -> None:
        items = [self.generate() for _ in range(self.M)]
        self.population = np.array([self.encode(item) for item in items])

    def encode(self, item: List[float]) -> str:
        chromosome = ""
        x, y = item
        x_length = int(self.l / 2)
        y_length = self.l - x_length
        chromosome = str(bin(int(x)))[2: x_length + 2] + str(bin(int(y)))[2: y_length + 2]
        return chromosome

    def decode(self, chromosome: str) -> List[float]:
        x_length = int(self.l / 2)
        y_length = self.l - x_length
        x = float(int(chromosome[:x_length], 2))
        y = float(int(chromosome[x_length:], 2))
        return [x, y]

    def f(self, chromosome: str) -> float:
        X = self.decode(chromosome)
        return self.target(*X)

    def cross(self, chromosome_1: str, chromosome_2: str, index: int) -> Tuple[str, str]:
        chromosome_1, chromosome_2 = chromosome_1[:index] + chromosome_2[index:], chromosome_2[:index] + chromosome_1[index:]
        return chromosome_1, chromosome_2

    def main(self) -> Tuple[str, float]:
        self.init_population()

        for t in range(self.T):
            fitness_values = np.array([self.f(individual) for individual in self.population])
            population_fitness = np.column_stack((self.population, fitness_values))

            for i in range(int(self.M / 2)):  # 选择算子
                fitness_sum = fitness_values.sum()
                probabilities = fitness_values / fitness_sum
                selected_indices = np.random.choice(self.M, size=self.M, p=probabilities)
                self.population = self.population[selected_indices]

            for i in range(0, self.M, 2):  # 交叉算子
                if np.random.uniform(0, 1) < self.pc:
                    index = np.random.randint(0, self.l)
                    self.population[i], self.population[i + 1] = self.cross(self.population[i], self.population[i + 1], index)

            for j in range(self.M):  # 变异算子
                if np.random.uniform(0, 1) < self.pm:
                    index = np.random.randint(0, self.l)
                    item = list(self.population[j])
                    item[index] = str(1 - int(item[index]))
                    self.population[j] = "".join(item)

        # 输出最高适应度的个体和函数值
        fitness_values = np.array([self.f(individual) for individual in self.population])
        best_individual_index = np.argmax(fitness_values)
        best_individual = self.population[best_individual_index]
        best_fitness = fitness_values[best_individual_index]

        return best_individual, best_fitness



SGA = SGA()
SGA.set_params(target=target, pc=0.6, pm=0.01, M=100, T=100)
best_individual, best_fitness = SGA.main()
print(f"Best individual: {best_individual}, Best fitness: {best_fitness}")