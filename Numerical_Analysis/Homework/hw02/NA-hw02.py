from math import sqrt

def g(x):
    return sqrt(10/(4+x))

def f(x):
    return 1/2*sqrt(10-x**3)

def newton_f(x):
    return (2*x**3-x**2+1)/(3*x**2-2*x)

n = 10
x0 = 1.5
xLst = [x0]
err = []
for _ in range(n):
    y0 = newton_f(x0)
    xLst.append(y0)
    err.append(abs(y0-x0))
    x0 = y0
    
print(xLst)
print(err)

