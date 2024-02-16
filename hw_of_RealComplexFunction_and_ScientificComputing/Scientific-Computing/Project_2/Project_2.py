import math
import matplotlib.pyplot as plt
import numpy as np

#函数
def f(x):
    return math.e**(-x**2)

#梯形公式 用逐次分半法
def T(f,a,b,N):#N=2^n
    global T_lst 
    T_lst = {0:(b-a)*(f(a)+f(b))/2}
    n = int(math.log(N,2))
    h = (b-a)/N
    if n==0:
        return T_lst[0]
    else:
        R = 0
        for i in range(1,2**(n-1)+1):
            R += f(a+(2*i-1)*h)
        return 1/2*T(f,a,b,int(N/2))+h*R
    
def Romberg(f,a,b,N,m):#外推m次
    n = int(math.log(N,2))
    mat_lst = [[T(f,a,b,2**k) for k in range(n+1)]]

    for i in range(m):
        mat_lst.append([0 for k in range(n+1)])

    
    for row in range(1,m+1):
        for line in range(0,n-row+1):
            mat_lst[row][line] = (4**row*mat_lst[row-1][line+1]-mat_lst[row-1][line])/(4**row-1)

    return mat_lst[m][n-m]

print(2/math.sqrt(math.pi)*Romberg(f,0,1,256,8))





    
  

