import math

def f(k):
    return math.comb(20,k)*(0.7)**k*(0.3)**(20-k)

print(sum([f(k) for k in range(0,10)]))
print(sum([f(k) for k in range(10,21)]))
