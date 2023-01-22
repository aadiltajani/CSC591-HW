import math

class SYM:
    def __init__(self,c=0,s='') -> None:
        self.n = 0
        self.has={}
        self.most=0
        self.mode = None

    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self.has[v] = 1 + self.has.get(v, 0)
            if self.has[v] > self.most:
                self.most = self.has[v]
                self.mode = v

    def mid(self):
        return self.mode

    def div(self):
        fun = lambda p : p*math.log(p,2)
        e = 0  
        for key in self.has.keys():
            if self.has[key] > 0 :
                e = e - fun(self.has[key]/self.n)
        
        return e