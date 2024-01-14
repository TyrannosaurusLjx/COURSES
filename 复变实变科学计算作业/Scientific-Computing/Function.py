# x_lst = [100, 105, 110, 115, 120]
# y_lst = [10, 10.246951, 10.488088, 10.723805, 10.954451]


# x_lst = [0,1,4,9,16,25,36,49,64,81,100]
# y_lst = [0,1,2,3,4,5,6,7,8,9,10]

# x_lst = [0,1,2,3,4]
# y_lst = [3,0,1,6,15]

# print(Lagrange(x_list=x_lst,y_list=y_lst)(115))
# print(Newton(x_list=x_lst,y_list=y_lst)(115))


# xst = [0,1,2,3,4]
# yst = [3,9,17,27,39]
# zlt = [5,7,9,11,13]
# print(Hermite(x_list=xst,y_list=yst,z_list=zlt)(5))

# xlst = [0,1,2]
# ylst = [0,1,3]
# print(Piecewise_Linear(x_list=xlst,y_list=ylst,x_0=1.5))


# xst = [0,1,2,3,4]
# yst = [3,9,17,27,39]
# zlt = [5,7,9,11,13]
# print(Piece_Hermite(xst,yst,zlt,2.5)(2.5))
# print(Hermite(x_list=xst,y_list=yst,z_list=zlt)(2.5))



import copy
#lagrange
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
    import numpy as np
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


#Newton插值多项式
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
    import numpy as np

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
    import numpy as np
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
    import numpy as np
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
    import numpy as np

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
    
    return piece_hermit_dict[index]





























