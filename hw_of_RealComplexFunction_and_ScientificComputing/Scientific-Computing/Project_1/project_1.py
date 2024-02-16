import time
import copy
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
#lagrange函数定义
def Lagrange(x_list,y_list):
    n = len(x_list)
    result = Lagrange_basefunction_list(x_list,n)
    return sum([result[i]*y_list[i] for i in range(n)])

#基函数列
def Lagrange_basefunction_list(x_list,n):
    result = []
    for i in range(n):
        result.append(Lagrange_basefunction(x_list,i))
    return result    

#基函数
def Lagrange_basefunction(x_list,i):
    X_list = copy.deepcopy(x_list)
    x_i = X_list[i]
    del X_list[i]
    #计算分母:
    denominator = 1
    for item in X_list:
        denominator = denominator*(x_i-item)

    #计算分子函数的系数
    coefficients_1 = np.poly(X_list)

    #计算函数系数
    coefficients_2 = [value/denominator for value in coefficients_1]

    #基函数
    basefunc = np.poly1d(coefficients_2,r = False ,variable='x')
    return basefunc


#Newton插值函数
def Newton(x_list,y_list):
    #构造均差表
            #n+1维的矩阵
    dim = len(x_list)
    mat = list([j for j in range(dim)] for i in range(dim))#给空列表赋了dim个值,不然空列表无法指定位置赋值
    #定义差商函数
    def f(i,j):
        if j==0:
            return y_list[i]
        else:
            return (f(i-1,j-1)-f(i,j-1))/(x_list[i-j]-x_list[i])
    #计算矩阵
    for i in range(len(x_list)):
        for j in range(i+1):
            mat[i][j] = f(i,j)

    #定义返回x的多项式的函数

    def N(k):
        func = 1
        if k == 0:
            pass
        else:
            func = np.poly1d(x_list[0:k],r = True ,variable = 'x')
        return func

    #返回最终的多项式
    newton = 0
    for i in range(dim):
        newton += N(i)*mat[i][i]
    return newton



#Hermite插值
def Hermite(x_list,y_list,z_list):
    n = len(x_list)-1
    #H(x)=\sum (y_i*h_i+y'_i*H_i)
    #计算h_i(x)前面的项
    #h_i
    def h(x_list,i):
        f = 0
        x_i = x_list[i]
        for j in range(n+1):
            if j!=i:
                f += 2*(np.poly1d([x_i],r=True,variable='x')/(x_list[j]-x_i))
            else:
                pass
        return (1+f)*Lagrange_basefunction(x_list,i)**2
    
    #H_i
    def H(x_list,i):
        return np.poly1d([x_list[i]],r=True,variable = 'x')*Lagrange_basefunction(x_list,i)**2
    
    #输出
    hermite = 0
    for i in range(n+1):
        hermite += y_list[i]*h(x_list,i)+z_list[i]*H(x_list,i)
    return hermite


#分段线性插值
def Piecewise_Linear(x_list,y_list,x_0):
    n = len(x_list)-1
    #定义区间函数
    def interval(x_list,x):
        for index in range(n):
            if x_list[index] <= x <=x_list[index+1]:
                return index
            else:
                pass

    #定义区间函数和函数字典
    def phi(x_list,y_list,i):
        f = y_list[i]*np.poly1d([x_list[i+1]],r=True,variable='x')/(x_list[i]-x_list[i+1])+\
        y_list[i+1]*np.poly1d([x_list[i]],r=True,variable='x')/(x_list[i+1]-x_list[i])
        return f
    phi_dict = {i:phi(x_list,y_list,i) for i in range(n)}
    #找出x所在的位置
    index = interval(x_list,x_0)
    return phi_dict[index]

#分段hermite插值
def Piece_Hermite(x_list,y_list,z_list,x_0):
    n = len(x_list)-1
        #定义区间函数
    def interval(x_list,x):
        for index in range(n):
            if x_list[index] <= x <=x_list[index+1]:
                return index
            else:
                pass
        #定义每一段上的插值函数
    def piece(x_list,y_list,z_list,i):
        x_lst = [x_list[i],x_list[i+1]]
        y_lst = [y_list[i],y_list[i+1]]
        z_lst = [z_list[i],z_list[i+1]]
        return Hermite(x_list=x_lst,y_list=y_lst,z_list=z_lst)
        #函数字典
    piece_hermit_dict = {i:piece(x_list,y_list,z_list,i) for i in range(n)}
    
    #找出x的位置
    index = interval(x_list,x_0)
    return piece_hermit_dict[index]#返回区间函数




n = max(10,int((input("请输入你的学号:\n"))[-1]))



def f(x):
    return 1/(1+25*x**2)

def diff_f(x):
    return -50*x/(1+25*x**2)**2

#用于绘制原函数
x_lst = np.arange(-1,1,0.001)
y_lst = f(x_lst)


#a
print('现在是项目a')
time.sleep(2)
x_list_1 = []
y_list_1 = []
for i in range(n+1):
    x_i = -1+2*i/n
    x_list_1.append(x_i)
    y_list_1.append(f(x_i))

Lagrange_1 = Lagrange(x_list=x_list_1,y_list=y_list_1)
Newton_1 = Newton(x_list=x_list_1,y_list=y_list_1)

#绘制langrange插值结果
x_1_L = np.arange(-1,1,0.01)
y_1_L = Lagrange_1(x_1_L)
plt.plot(x_lst,y_lst)
plt.title('Lagrange Interpolation')
plt.plot(x_1_L,y_1_L)
plt.xlabel('x')
plt.ylabel('lagrange_1')
for i in range(n+1):
    plt.scatter(x_list_1[i],y_list_1[i])
plt.axis('on')
plt.show()

#绘制newton插值结果
x_1_N = np.arange(-1,1,0.01)
y_1_N = Newton_1(x_1_N)
plt.plot(x_lst,y_lst)
plt.title('Newton Interpolation')
plt.plot(x_1_N,y_1_N)
plt.xlabel('x')
plt.ylabel('Newton_1')
for i in range(n+1):
    plt.scatter(x_list_1[i],y_list_1[i])
plt.axis('on')
plt.show()



#b
print('现在是项目b')
time.sleep(2)
#定义插值节点函数
def g(x):
    import math
    return math.cos((2*x+1)*math.pi/42)
#作出插值节点和对应函数值
x_list_2 = []
y_list_2 = []
for i in range(21):
    x_i = g(i)
    x_list_2.append(x_i)
    y_list_2.append(f(x_i))
#作出Lagrange插值函数
Lagrange_2 = Lagrange(x_list=x_list_2,y_list=y_list_2)
#绘图
x_2_L = np.arange(-1,1,0.01)
y_2_L = Lagrange_2(x_2_L)
plt.plot(x_lst,y_lst)
plt.title('Lagrange Interpolation')
plt.plot(x_2_L,y_2_L)
plt.xlabel('x')
plt.ylabel('lagrange_2')
for i in range(21):
    plt.scatter(x_list_2[i],y_list_2[i])
plt.axis('on')
plt.show()

#c
print('现在是项目c')
time.sleep(2)
#计算插值节点
x_list_3 = [-1+2*i/10 for i in range(11)]
y_list_3 = [f(-1+2*i/10) for i in range(11)]
#计算插值函数
x_lst_3 = np.arange(-1,1,0.01)
y_lst_3 = []
for x in x_lst_3:
    y_lst_3.append(Piecewise_Linear(x_list=x_list_3,y_list=y_list_3,x_0=x)(x))
#绘图
plt.title('Piecewise Linear Interpolation')
for i in range(11):
    plt.scatter(x_list_3[i],y_list_3[i])
plt.plot(x_lst,y_lst)
plt.xlabel('x')
plt.ylabel('Piecewise Linear')
plt.plot(x_lst_3,y_lst_3)
plt.show()

#d
print('现在是项目d')
time.sleep(2)
#计算插值节点
x_list_4 = [-1+2*i/10 for i in range(11)]
y_list_4 = [f(-1+2*i/10) for i in range(11)]
z_list_4 = [diff_f(-1+2*i/10) for i in range(11)]

#计算分段hermite插值函数
x_lst_4 = np.arange(-1,1,0.01)
y_lst_4 = []
for x in x_lst_4:
    y_lst_4.append(Piece_Hermite(x_list=x_list_4,y_list=y_list_4,z_list=z_list_4,x_0=x)(x))

#绘图
plt.title('Piecewise Hermite Interpolation')
plt.plot(x_lst,y_lst)
for i in range(11):
    plt.scatter(x_list_4[i],y_list_4[i])
plt.xlabel('x')
plt.ylabel('Piecewise Hermite')
plt.plot(x_lst_4,y_lst_4)
plt.show()

