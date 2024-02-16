import numpy as np
dim = 3




def getPQ(i, j, k, l):
    P = np.eye(dim)
    Q = np.eye(dim)
    P[[i,k]] = P[[k,i]]
    Q[:,[j,k]] = Q[:,[k,j]]
    return P, Q


P,Q = getPQ(0,0,1,1)
print(P,Q)
