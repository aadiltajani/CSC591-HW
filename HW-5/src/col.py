import NUM
import sym

def col(n,s):
    if s[0].isupper():
        col = sym.sym(n,s)
    else:
        col = NUM.NUM(n,s)

    col.isIgnored = s.endswith('X')
    col.isKlass = s. endswith(';')
    col.isGoal = s.endswith('!') or s.endswith('+') or s.endswith('-')

    return col