import math
# \xi ~ B(n,p),定义P（\xi = k)
def binomial_P(n,p,k):
    result = math.comb(n,k) * (p**k) * (1-p)**(n-k)
    return result

# P(\xi\geq k)
def binomial_geq_k_P(n,p,k):
    P_lst =[binomial_P(n,p,i) for i in range(k,n+1)]
    result = sum(P_lst)
    return result

# p(\xi\leq k)
def binomial_leq_k_P(n,p,k):
    return 1-binomial_geq_k_P(n,p,k+1)



