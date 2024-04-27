from math import trunc
import random 


class RandomWalk:
    def __init__(self) -> None:
        self.p = 0
        self.trace = []

    
    def set_value(self, p):
        self.p = p

    def Xi(self):
        if random.uniform(0,1) < self.p:
            return 1
        else:
            return -1

    def Sn(self, n):
        s = 0
        for _ in range(n):
            s += self.Xi()
        return s

    def trace_s(self, n):
        s = 0
        trace = [s]
        for _ in range(n):
            s += self.Xi()
            trace.append(s)
        return trace

    def run(self, iter, n):
        all_traces = [0 for i in range(iter)]
        for i in range(iter):
            all_traces = [ x + y for x,y in zip(all_traces, self.trace_s(n)) ]
        self.trace = [ item/n for item in all_traces ]
        return self.trace

    def main(self,iter,n):
        return self.run(iter, n)

r1 = RandomWalk()
r1.set_value(0.5)
print(r1.main(10000,10))






