class SA_TSP():
    from random import sample, choice, choices, uniform
    def __init__(self, C):
        self.maxDepth = 5 # 最大迭代深度
        self.target = 1 # 目标优化值
        self.dim = len(C) # 维度
        self.Top = self.dim * max(max(row) for row in C)
        self.C = C # 距离矩阵
        self.Pm = 0.1
        self.Pc = 0.5
        self.Py = 1 - self.Pm - self.Pc
        # 每个sigma是一个list
        self.sigmas = []
    
    # def check(self,sigma,func):
    #     if set(sigma) != set(range(self.dim)):
    #         print("here is wrong,func is ",func)
    #     exit(-1)    
        
    # 种群初始化
    def setX(self, target = 1 , X0 = [], depth = 1000,):
        if len(X0) == 0:
            self.sigmas.append(self.sample(range(self.dim),self.dim))
        else:
            self.sigmas = X0
        self.maxDepth = depth
        self.target = target 
    
    # 设置种群行为概率
    def setProbability(self, Pc, Pm):
        self.Pm = Pm
        self.Pc = Pc
        self.Py = 1 - Pm - Pc
    
    # 染色体编码
    def code(self, S):
        # 设定起点都在城市0
        current_city = 0
        chromosome = [current_city]
        while len(chromosome) < self.dim:
            next_city = [col for col in range(self.dim) if S[current_city][col] == 1][0] # 找出下一个城市
            current_city = next_city
            chromosome.append(current_city)
        return chromosome
    
    # 舒适度
    def comfort(self, sigma):
        S = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(len(sigma)-1):
            S[sigma[i]][sigma[i+1]] = 1
        S[sigma[-1]][sigma[0]] = 1 
        s = self.Top - sum([self.C[i][j] for  i in range(self.dim) for j in range(self.dim) if S[i][j] == 1])
        return s
    
    # 复制函数
    def Copy(self):
        newSigma = self.choices(self.sigmas, [self.comfort(sigma) for sigma in self.sigmas])[0]
        return newSigma
    
    # 选择函数
    def Select(self):
        father,mather = self.choices(self.sigmas, [self.comfort(sigma) for sigma in self.sigmas], k=2)
        # son = [-1 for _ in range(self.dim)]
        # # 根据概率选择
        # for value in range(16):
        #     # print(value)
        #     x = self.uniform(0,1)
        #     p = self.comfort(father)/(self.comfort(father) + self.comfort(mather))
        #     fatherIndex = father.index(value)
        #     matherIndex = mather.index(value)
        #     if x<p:
        #         if son[fatherIndex] == -1 :
        #             son[fatherIndex] = value
        #         else:
        #             son[matherIndex] = value
        #     else:
        #         if son[matherIndex] == -1:
        #             son[matherIndex] = value
        #         else:
        #             son[fatherIndex] = value
        son = father if self.comfort(father) > self.comfort(mather) else mather
        return son

    
    # 突变函数
    def Mutation(self):
        newSigma = self.choice(self.sigmas)
        i,j = self.choices(range(self.dim),k=2)
        i,j = min(i,j),max(i,j)
        newSigma[i],newSigma[j] = newSigma[j],newSigma[i]
        return newSigma
    
    # 获取当前种群中的最优种群舒适度
    def best(self):
        a = max([self.comfort(sigma) for sigma in self.sigmas])
        return a
    
    def main(self):
        if len(self.sigmas) == 0:
            self.setX()
        # 当前迭代深度
        depth = 0
        while depth < self.maxDepth and self.best() > self.target:
            newSigmas = []
            for _ in range(self.dim):
                # comfortLevel = [self.comfort(sigma) for sigma in self.sigmas]
                rNum = self.uniform(0,1)
                
                if rNum < self.Py : # 复制
                    newSimga = self.Copy()
                elif rNum < self.Py + self.Pc:
                    newSimga = self.Select()
                else:
                    newSimga = self.Mutation()
                newSigmas.append(newSimga)
            depth += 1
            self.sigmas = newSigmas
        return self.Top - self.best() # 1018左右
        
      
import math
city = [(12,12),(18,23),(24,21),(29,25),(31,52),(36,43),(37,14),(42,8),(51,47),\
    (62,53),(63,19),(69,39),(81,7),(82,18),(83,40),(88,30)]
# city = [(0,0),(1,1),(3,4)]

def d(i,j):
    city1,city2 = city[i],city[j]
    return math.sqrt( math.pow(city1[0]-city2[0], 2) + math.pow( city1[1] - city2[1] ,2) )

M = [[0 for _ in range(len(city))] for _ in range(len(city))]

for i in range(len(city)):
    for j in range(len(city)):
        M[i][j] = d(i,j)
        
b = SA_TSP(M)
b.setX(target=200,X0=[],depth=1000)
b.setProbability(Pc=0.4,Pm=0.05)

result = b.main()
print("top = ",b.Top,"   target = ",b.target, "  best = ", b.best())
print(result)


