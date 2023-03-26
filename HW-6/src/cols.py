import sys
# sys.path.append("./code")
import col as c
import SYM
# def cols(ss):
#     cols={'names' : ss,
#     'all': [],
#     'x': [],
#     'y': []}

#     for n,s in enumerate(ss):
        
#         col1 = c.col(n, s)
#         cols["all"].append(col1)
#         if not col1['isIgnored']:
#             if col1['isKlass']:
#                 cols['klass'] = col1
#             if col1['isGoal']:
#                 cols["y"].append(col1)
#             else:
#                 cols["x"].append(col1)
#     return cols


class Cols:
    def __init__(self, ss):
        self.names = ss
        self.all = []
        self.x = []
        self.y = []
        for n, s in enumerate(ss):
            col = c.Col(n, s)
            self.all.append(col)
            if not col.isIgnored:
                if hasattr(col, 'isKlass') and col.isKlass:
                    self.klass = col
                if col.isGoal:
                    self.y.append(col)
                else:
                    self.x.append(col)
    


