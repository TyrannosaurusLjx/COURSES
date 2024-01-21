import distance as dis
import numpy as np

x = np.array(list(range(7)))
y = np.array(list(range(3,10)))

z = np.array([[i*j for i in range(1,8)] for j in range(4)])

print(dis.Dis(x,z,dis.F))
