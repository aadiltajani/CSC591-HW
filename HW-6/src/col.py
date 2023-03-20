import NUM
import SYM

def col(n,s):
    is_num = s[0].isupper()
    col = NUM.num(n, s) if is_num else SYM.SYM(n, s)
    col['isIgnored'] = s.endswith("X")
    col['isKlass'] = s.endswith("!")
    col['isGoal'] = s.endswith("!") or s.endswith("+") or s.endswith("-")
    
    return col