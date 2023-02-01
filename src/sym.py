import math


class sym:
    def __init__(self, at=0, txt='') -> None:
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None
        self.at = at
        self.txt = txt

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
        fun = lambda p: p * math.log(p, 2)
        e = 0
        for key in self.has.keys():
            if self.has[key] > 0:
                e = e - fun(self.has[key] / self.n)
        return e

    def rnd(self, v, n):
        return v

    def dist(self,s1,s2):
        if s1 == '?' and s2 == '?':
            return 1
        elif s1==s2:
            return 0
        else:
            return 1
