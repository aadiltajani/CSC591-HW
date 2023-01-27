import sys
import math
import functions

class NUM:
    def __init__(self, at=0, txt=''):
        self.n = 0
        self.at = at
        self.txt = txt
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.w = -1 if '-' in self.txt else 1

    def add(self, n):
        # if isinstance(n, float) or isinstance(n, int):
        if n != '?':
            self.n += 1
            d = n - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        if self.m2 < 0 or self.n < 2:
            return 0
        return math.sqrt(self.m2 / (self.n - 1))

    def rnd(self, x, n):
        return x if x == "?" else functions.rnd(x, n)
