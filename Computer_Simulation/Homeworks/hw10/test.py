import numpy as np
from itertools import permutations 
from random import choice, choices, sample
class perm():

    def __init__(self, n, m):
        self.Pm = 0.01
        self.Pc = 0.4
        self.T = 100
        self.target = 10000
        self.n = n
        self.m = m
        self.perms = []
        
    # 产生n:m的0-1矩阵
    def getMatrix(self):
        matrix = np.zeros((self.n, self.n))
        indices = np.random.choice(self.n*self.n, self.m, replace=False)
        matrix.flat[indices] = 1
        return matrix
    
    # 随机生成初始值
    def setInitial(self):
        for _ in range(12):
            self.perms.append(self.getMatrix())
    
    # 积和式值 适应度
    def getFitness(self, matrix):
        if any( [ sum([matrix[i][j] for j in range(self.n) ]) == 0 for i in range(self.n)] )  or \
            any( [ sum([matrix[i][j] for i in range(self.n)]) == 0 for j in range(self.n) ] ) :
            perm_sum = 0
        else:
            perm_sum = 0  
            all_permutations = permutations(range(self.n))  
            for permutation in all_permutations:  
                product = 1  
                for i in range(self.n):  
                    product *= matrix[i, permutation[i]]  
                perm_sum += product  
        return perm_sum  


    
    # 突变
    def mutation(self):  
        print("mutations now")
        newMatrix = choices(self.perms,[self.getFitness(perm) for perm in self.perms])[0]  
        i, j = sample(range(self.n), 2)  
        direction = choice(['N', 'W', 'S', 'E'])  
        
        # 获取当前位置和相邻位置的值  
        current = newMatrix[i][j]  
        if direction == 'N':  
            next_i = (i - 1) % self.n  
            newMatrix[i][j], newMatrix[next_i][j] = newMatrix[next_i][j], current  
        elif direction == 'W':  
            next_j = (j - 1) % self.n  
            newMatrix[i][j], newMatrix[i][next_j] = newMatrix[i][next_j], current  
        elif direction == 'S':  
            next_i = (i + 1) % self.n  
            newMatrix[i][j], newMatrix[next_i][j] = newMatrix[next_i][j], current  
        else:  # direction == 'E'  
            next_j = (j + 1) % self.n  
            newMatrix[i][j], newMatrix[i][next_j] = newMatrix[i][next_j], current  
        
        return newMatrix 
    # 交叉
    def crossover(self):
        print("crossover now")
        A,B = choices(self.perms,[self.getFitness(perm) for perm in self.perms],k=2)
        Alst = list(A.flat)
        Blst = list(B.flat)
        i,j = sample(range(self.n*self.n),2)
        Alst = Alst[i:] + Alst[:i]
        Blst = Blst[j:] + Blst[:j]
        for index in range(self.n * self.n):
            if Alst[index] != Blst[index]:
                Alst[index],Blst[index] = Blst[index],Alst[index]
        C = np.array(Alst).reshape(self.n,self.n)
        return C
    
    # 选择
    def copy(self):
        print("copy now")
        newMatrix = choices(self.perms,[self.getFitness(perm) for perm in self.perms])[0]
        return newMatrix
    
    # 获取当前种群中的最优种群舒适度
    def best(self):
        print("get best now")
        BestComfort = max([self.getFitness(perm) for perm in self.perms])
        print("finish get best")
        return BestComfort
    
    # 主函数
    def main(self):
        print("begin !")
        self.setInitial()
        print("initial finished")
        depth = 0
        while depth < self.T and self.best() < self.target:
            print("now depth",depth)
            newPerms = []
            for _ in range(self.m):
                rNum = np.random.rand()
                if rNum < self.Pm:
                    newPerm = self.mutation()
                elif rNum < self.Pc + self.Pm:
                    newPerm = self.crossover()
                else:
                    newPerm = self.copy()
                newPerms.append(newPerm)
            depth += 1
            self.perms = newPerms
        return self.best()
    
a = perm(8,20)
result = a.main()
print("final result",result)