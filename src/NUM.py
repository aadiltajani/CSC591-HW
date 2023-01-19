class NUM: 
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf
        
    def add(self, n):
        if (isinstance(n, int)):
            #if n != '?':
            self.n += n
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
    
    def mid(self, x):
        return self.mu
    
    def div(self, x):
        if (self.m2 < 0 or self.n ):
            return 0
        return math.sqrt(self.m2/(self.n - 1))
