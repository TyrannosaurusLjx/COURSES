import numpy as np
import matplotlib.pyplot as plt

#定义被插值函数
def f(x):
    return 1/(1+25*x**2)

#定义插值函数
def Lagrange(x_list,y_list):
    n = len(x_list)
    result = Lagrange_basefunction_list(x_list,n)
    return sum([result[i]*y_list[i] for i in range(n)])

#定义基函数列
def Lagrange_basefunction_list(x_list,n):
    result = []
    for i in range(n):
        result.append(Lagrange_basefunction(x_list,i))
    return result    

#定义基函数
def Lagrange_basefunction(x_list,i):
    X_list = np.delete(x_list, i)

    #计算分母:
    denominator = 1
    for item in X_list:
        denominator *= (x_list[i]-item)

    #计算分子函数的系数
    coefficients_1 = np.poly(X_list)

    #计算函数系数
    coefficients_2 = [value/denominator for value in coefficients_1]

    #基函数
    basefunc = np.poly1d(coefficients_2,r = False ,variable='x')
    return basefunc

#插值点
n = 20
x_list = []
for i in range(n):
    x_list.append(-1+2*i/n)
y_list = []
for i in x_list:
    y_list.append(f(i))

Lagrange1 = Lagrange(x_list,y_list)

y = [Lagrange1(i) for i in x_list]

plt.plot(x_list, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Graph')
plt.show()

plt.show()
