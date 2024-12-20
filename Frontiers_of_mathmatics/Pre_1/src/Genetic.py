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


    def set_params(self,target: callable, pc = 0.6: float, pm = 0.01: float, M = 100: int, T = 1000: int, f: callable, encode: callable, decode: callable, ranges: list[float]) -> None:
        self.target = target
        self.pc = pc
        self.pm = pm
        self.M = M
        self.T = T
        self.f = f
        self.encode = encode
        self.decode = decode
        self.ranges = ranges

    def generate(self) -> list:
        return  np.array( [np.random.uniform(self.ranges[0], self.ranges[1]), np.random.uniform(self.ranges[2], self.ranges[3])] )

    def init_population(self) -> None:
        items = np.array( [ self.generate() for _ in range(self.M) ] )
        self.population = np.array( [ self.encode(item) for item in items ] )
    
    def encode(self, item: list) -> str:
        chromosome = ""
        x, y = item
        x_length = int(self.l/2)
        y_length = self.l - x_length
        chromosome = str(bin(x))[2: x_length+2] + str(bin(y))[2: y_length + 2]
        return chromosome
    
    def decode(self, chromesome: str) -> list:
        x_length = int(self.l/2)
        y_length = self.l - x_length
        x = float(int(chromesome[:x_length],2))
        y = float(int(chromesome[x_length:],2))
        return np.array([x,y])
    
    def f(self, chromesome: str) -> float:
        X = self.decode(chromesome)
        return self.target(X)
    
    def cross(self, chromesome_1: str, chromesome_2: str, index: int) -> list:
        chromesome_1, chromesome_2 = chromesome_1[:index] + chromesome_2[index:], chromesome_2[:index] + chromesome_1[index:]
        return chromesome_1, chromesome_2
        
        
    
    def main(self) -> float:
        self.init_population()

        
        for t in range(self.T):
            fitness_values = np.array([self.f(individual) for individual in self.population])
            population_fitness = np.column_stack(self.population, fitness_values)
            
            for i in range(int(self.M / 2)): # 选择算子
                fitness_sum = fitness_values.sum()
                self.population[i] = np.random.choice(population_fitness[:,0], p=fitness_values/fitness_sum)
            
            for i in range(i, self.M, 2): # 交叉算子
                cross_1, cross_2 = population_fitness[i], population_fitness[i+1]
                if np.random.uniform(0,1) < self.pc:
                    index = np.random.randint(0, self.l)
                    cross_1, cross_2 = self.cross(cross_1, cross_2, index)
                    self.population[i], self.population[i+1] = cross_1, cross_2
            
            for j in range(self.M): #变异算子
               if np.random.uniform(0,1) < self.pm:
                    index = np.random.randint(0, self.l)
                    item = self.population[j]
                    item = list(item)
                    item[index] = ( 1-int(item[index]) )
                    item = "".join(item)
                    self.population[j] = item
        
        # 输出最高适应度的个体和函数值
        fitness_values = np.array([self.f(individual) for individual in self.population])
        population_fitness = np.column_stack(self.population, fitness_values)
        # 找到适应度值最高的个体
        best_individual_index = np.argmax(fitness_values)
        best_individual = self.population[best_individual_index]
        best_fitness = fitness_values[best_individual_index]

        return best_individual, best_fitness
                    
                        
SGA = SGA()
SGA.set_params(target=target,pc=0.6,pm=0.01,M=100,T=100)
SGA.main()          
                        
                
            
            

                
    
    





















