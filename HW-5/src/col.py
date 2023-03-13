import NUM
import SYM

def col(n,s):
    if not s[0].isupper():
        col = SYM.SYM(n,s)
    else:
        col = NUM.num(n,s)

    col.isIgnored = s.endswith('X')
    col.isKlass = s. endswith(';')
    col.isGoal = s.endswith('!') or s.endswith('+') or s.endswith('-')

    return col