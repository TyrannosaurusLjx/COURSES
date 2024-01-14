import numpy as np
from scipy.optimize import minimize

def f(x):
    return -2*x/(1+x**2)**2 * np.cos(1/(1+x**2)**2)

result = minimize(f,x0=1)
print(result)
