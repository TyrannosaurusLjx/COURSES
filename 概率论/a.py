import random as rd  
  
def test():  
    ls = [rd.choices([1, 2, 3])[0] for _ in range(1000)]  
    result = 0  
    for k in ls:  
        if k == 1:  
            result += 3  
            break  
        elif k == 2:  
            result += 5  
        else:  
            result += 7  
    return result  
  
r = []  
for _ in range(10000):  
    r.append(test())  
  
print(sum(r) / 10000)  