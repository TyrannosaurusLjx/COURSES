import numpy as np  
  
def tent_ode(x, u, M):  
    ret = np.zeros(M)  
    ret[0] = x  
      
    for i in range(1, M):  
        if ret[i-1]< 0.5:  
            ret[i] = 2 * u * ret[i-1]  
        else:  
            ret[i] = 2 * u * (1 - ret[i-1])  
      
    return ret  
  
M = 102400  
ret = tent_ode(0.1, 0.99, M)  
rand_bin_stream = np.floor(np.mod(ret * 100, 2))  
  
with open("rbs", "wb") as fid:  
    tmp = 0  
    for i in range(M):  
        if i % 8 != 0:  
            tmp = tmp + rand_bin_stream[i] * 2**(8 - (i % 8))  
        else:  
            tmp = tmp + rand_bin_stream[i]  
            fid.write(bytes([int(tmp)]))  
            tmp = 0  