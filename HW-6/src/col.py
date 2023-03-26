import NUM
import SYM

class Col:
    def __init__(self, n, s):
        self.col = NUM.Num(n, s) if s[0].isupper() else SYM.sym(n, s)
        self.isIgnored = self.col.txt.endswith("X")
        self.isKlass = self.col.txt.endswith("!")
        self.isGoal = self.col.txt[-1] in ["!", "+", "-"]