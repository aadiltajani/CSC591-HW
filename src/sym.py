import math

class sym:
    def __init__(self,c=0,s='') -> None:
        self.n = 0
        self.has={}
        self.most=0
        self.mode = None

    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self._has[v] = 1 + self._has.get(v, 0)
            if self.has[v] > self.most:
                self.most = self.has[v]
                self.node = self.v

    def mid(self):
        return self.mode

    def div(self):
        fun = lambda p : p*math.log(p,2)
        e = 0  
        for key in self._has.keys():
            if self._has[key] > 0 :
                e = e - fun(self._has[key]/self.n)
        
        return e