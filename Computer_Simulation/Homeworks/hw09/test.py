import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# plt.rcParams['font.sans-serif'] = ['SimHei'] 
 
#自定义函数 
def func(x, a, b, c):
    return a * np.exp(b*x)/(1+(a/c)*np.exp(b*x))
 
#定义x、y散点坐标
x = np.array(range(10,220,10))
populations = [3929214,5308483,7239881,9638453,12866020,17069453,23191876,31433321,39818449,\
    50155783,62947714,75994575,91972266,105710620,122775046,131669275,151325798,179323175,\
        203302031,226545805,248709873]
populations = [item / 10**4 for item in populations]
y = np.array(populations)
#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
a = popt[0] 
b = popt[1]
c = popt[2]
yvals = func(x, a, b, c) #拟合y值

print('系数a:', a)
print('系数b:', b)
print('系数c:', c)

#绘图
fig = plt.figure(figsize = (10, 7))
plot1 = plt.plot(x, y, 's', label = '数据值')
plot2 = plt.plot(x, yvals, 'r',label = '拟合曲线')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'best') #指定legend的位置右下角
plt.title('最小二乘法拟合曲线')
plt.show()
