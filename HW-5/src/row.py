import sys
# sys.path.append("./code")
import data
import functions
import cols

def row(data,t):
    if data['cols']:
        data['rows'].append(t)
        for _,colss in [data['cols']['x'],data['cols']['y']]:
            for _,col in colss:
                functions.add(col, t[col.at])
    else:
        data['cols'] = cols.cols(t)

    return data


# class Row:

#     def __init__(self, t:list):
#         self.cells = t
#         self.x = None
#         self.y = None