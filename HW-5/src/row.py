import sys
# sys.path.append("./code")
import data
import functions
import col

def row(data,t):
    if data.cols:
        data['rows'] = t
        for _,cols in [data['cols']['x'],data['cols']['y']]:
            for _,cols in cols:
                functions.add(col, t[col.at])
    else:
        data.cols = cols(t)

    return data


# class Row:

#     def __init__(self, t:list):
#         self.cells = t
#         self.x = None
#         self.y = None