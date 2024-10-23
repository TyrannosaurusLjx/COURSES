import numpy as np

def target_function(X: np.array) -> float:
        x,y = X
        r = np.sqrt(np.abs(x**2 + y**2 + (x-y)**2*x))
        return 100 / (1 + np.exp(-r))
def rosenbrock(X: np.array) -> float:
    x, y = X
    a = 1
    b = 100
    r = - (a - x)**2 + b * (y - x**2)**2
    return 100 / (1 + np.exp(-r))



"""
采用浮点数编码,交叉算子采用单点交叉,变异算子采用单点变异
"""
class SGA():
    def __init__(self):
        self.pc = 0.6 # 交叉概率
        self.pm = 0.01 # 变异概率
        self.T = 1000 # 迭代次数
        self.N = 30 # 种群个数
        self.f = lambda X: 0 # 适应度函数
        self.L = 10 # 自变量维度
    
    
    def set_params(self, pc: float, pm: float, T: int, N: int, f, l: int):
        self.pc = pc
        self.pm = pm
        self.T = T
        self.N = N
        self.f = f
        self.L = l
        self.population = np.array([])

    def init_population(self):
        self.population = np.random.uniform(0,1,(self.N, self.L)) * 10 - 5
 
    
    # 编码函数
    def encode(self, X: np.array) -> np.array:
        return X
    
    # 解码函数
    def decode(self, X: np.array) -> np.array:
        return X

    # 选择函数
    def choose(self, population: np.array) -> np.array:
        n = len(population)
        values = np.array([self.f(self.decode(X)) for X in population])

        values = values / np.sum(values)

        values[-1] = 1 - np.sum(values[:-1])

        index = np.random.choice(n, n, p=values)
        
        return population[index]

    # 交叉函数 
    def cross(self, population: np.array) -> np.array:
        n = len(population)
        l = self.L

        new_population = []
        if n % 2 != 0:
            raise ValueError("reset population size")
        for i in range(0, n, 2):
            mom, dad = population[i], population[i+1]
            if np.random.uniform(0, 1) < self.pc:
                point = np.random.choice([i for i in range(l)])
                new_population.append(np.concatenate([mom[:point], dad[point:]]))
                new_population.append(np.concatenate([dad[:point], mom[point:]]))
            else:
                new_population.append(mom)
                new_population.append(dad)
        return np.array(new_population)
    
    # 变异函数
    def mutation(self, population: np.array) -> np.array:
        for i in range(len(population)):
            if np.random.rand() < self.pm:
                point = np.random.randint(self.L)
                value = population[i][point]
                population[i][point] += np.random.uniform(-3,3) 
        return population
    
 
    def run(self):
        self.init_population()
        for t in range(self.T):
            population = self.choose(self.population)
            population = self.cross(population)
            population = self.mutation(population)
            self.population = population

        best = np.argmax([self.f(self.decode(X)) for X in self.population])
        return self.f(self.decode(self.population[best]))


SGA = SGA()
SGA.set_params(pc=0.6, pm=0.01, T=1000, N=100, f=rosenbrock, l=2)
print(SGA.run())