from scipy.stats import uniform
import math
def f(x):
    result = 100*x**3
    return result

def g(x):
    return 3/2*math.sqrt(x)

def h(x):
    return f(x)/g(x)

def inverse_G(x):
    result = x**(2/3)
    return result

def IS(f,g,inverse_G, a,b):
    rvs = uniform.rvs(0,1,size = 100000)
    rvs = [inverse_G(rv) for rv in rvs]
    result = sum(h(rv) for rv in rvs)/len(rvs)
    return result

IS(f,g,inverse_G,0,1)