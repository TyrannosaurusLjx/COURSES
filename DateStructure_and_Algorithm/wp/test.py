import math
import random
def P(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(1,356))
    if len(set(lst)) != n:
        return False
    else:
        return True
total = 0
k = int(input())
for j in range(2,k):
    if P(j):
        total+=1
print(total/k)
