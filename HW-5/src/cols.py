import sys
# sys.path.append("./code")
import col as c
import SYM
def cols(ss):
    cols={'names' : ss,
    'all': [],
    'x': [],
    'y': []}

    for n,s in enumerate(ss):
        
        col1 = c.col(n, s)
        cols["all"].append(col1)
        if not col1['isIgnored']:
            if col1['isKlass']:
                cols['klass'] = col1
            if col1['isGoal']:
                cols["y"].append(col1)
            else:
                cols["x"].append(col1)
    return cols
    


# class Cols:

#     def __init__(self, names):
#         if(type(names) == dict):
#             temp = names.items()
#         else:
#             temp = enumerate(names)
#         self.names = names
#         self.all = []
#         self.x = []
#         self.y = []
#         self.klass = None

#         for k, column_name in temp:
#             if column_name[0].isupper():
#                 column = NUM(k, column_name)
#             else:
#                 column = sym(k, column_name)
#             self.all.append(column)
#             if column_name[-1] != 'X':
#                 self.klass = column_name
#                 if '+' == column_name[-1] or '-' == column_name[-1]:
#                     self.y.append(column)
#                 else:
#                     self.x.append(column)

#             # if column_name[-1] == '!':
#             #     self.klass = column
#             # self.all.append(column)

#     def add(self, row):
#         for t in [self.x, self.y]:
#             for col in t:
#                 col.add(row.cells[col.at])
