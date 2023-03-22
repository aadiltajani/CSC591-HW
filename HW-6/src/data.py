import math
import re
import sys
sys.path.append("./HW-6/src")
from typing import Iterable
import functions
import row
import cols as c
from functions import t, csv
# class DATA:
#     def __init__(self, src=None):
#         self.rows = []
#         self.cols = None

#         # if isinstance(src, str):
#         #     for x in functions.csv_read(src):
#         #         self.add(x)
#         # else:
#         #     # self.add(src)
#         #     functions.map(src, self.add)

#     # def add(self, t):
#     #     if self.cols:
#     #         t = t if hasattr(t, "cells") else row.Row(t)
#     #         self.rows.append(t)
#     #         self.cols.add(t)
#     #     else:
#     #         self.cols = cols.Cols(t)

#     def new(self):
#         return {'rows':[], 'cols':None}

#     def clone(self, data, ts, init=None):
#         data1 = row(self.new(), data['cols']['names'])
#         for i in ts:
#             row(data1, i)
#         return data1

#     def read(self, file):
#         data = self.new()
#         t = functions.csv_read(file)
#         for i in t:
#             row(data, i) 

    # def stats(self, what=None, cols=None, nPlaces=None):
    #     def fun(col):
    #         x = col.mid() if what == 'mid' else col.div()
    #         return col.rnd(x, nPlaces)

    #     return {col.txt: fun(col) for col in cols}

    # def better(self, row1, row2):
    #     s1, s2 = 0,0
    #     ys = self.cols.y
    #     for col in ys:
    #         x = col.norm(row1.cells[int(col.at)])
    #         y = col.norm(row2.cells[int(col.at)])
    #         s1 = s1 - math.exp(col.w * (x - y)/len(ys))
    #         s2 = s2 - math.exp(col.w * (y - x)/len(ys))
    #     if s1/len(ys) < s2/len(ys):
    #         return True
    #     else:
    #         return False


    # def dist(self, row1, row2, cols=None):
    #     n, d = 0, 0
    #     for _, col in enumerate(self.cols.x or cols):
    #         n = n + 1
    #         d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** 2
    #     return (d / n) ** (1 / 2)

    # def around(self, row1, rows=None, cols=None):
    #     if rows is None:
    #         rows = self.rows
    #     if isinstance(rows, Iterable):
    #         iterable = rows
    #     else:
    #         iterable = self.rows
    #     rows_with_distance = [(row2, self.dist(row1, row2, cols))
    #                           for row2 in iterable]
    #     sorted_rows = sorted(rows_with_distance, key=lambda x: x[1])
    #     return [(row, dist) for row, dist in sorted_rows]

    # def half(self, rows=None, cols=None, above=None):
    #     A, B, left, right, c, mid, some = None, None, None, None, None, None, None
        
    #     def project(row):
    #         x, y  = functions.cosine(dist(row, A), dist(row, B), c)
    #         row.x = x or row.x
    #         row.y = y or row.y
    #         return {'row': row, 'x': x, 'y': y}
    #     def dist(row1, row2, cols=None):         
    #         return self.dist(row1, row2, cols)
    #     rows = rows or self.rows
    #     A = functions.any(rows)
    #     B = self.furthest(A, rows)
    #     c = dist(A, B)
    #     left, right = [], []
    #     mapVAR = [project(row) for row in rows]
    #     sorted_rows = sorted(mapVAR, key=lambda x: x["x"])
    #     for n, tmp in enumerate(sorted_rows):
    #         if n <= len(rows) // 2 - 1:
    #             left.append(tmp["row"])
    #             mid = tmp["row"]
    #         else:
    #             right.append(tmp["row"])
    #     return left, right, A, B, mid, c
        
    # def cluster(self, rows=None, cols=None, above=None):
    #         rows = rows if rows else self.rows
    #         cols = cols if cols else self.cols.x
    #         node = {"data": self.clone(rows)}
            
    #         if len(rows) >= 2:
    #             left, right, node["A"], node["B"], node["mid"], node["C"] = self.half(rows, cols, above)
    #             node["left"] = self.cluster(left, cols, node["A"])
    #             node["right"] = self.cluster(right, cols, node["B"])
    #         return node

    # def sway(self, S = None, F = None, p = None, rows = None, min = None, cols = None, above = None):
    #     rows = rows if rows != None else self.rows
    #     cols = cols if cols != None else self.cols.x
    #     min = min if min != None else len(self.rows) ** 0.5 
    #     node = self.clone(rows)

    #     if len(rows) > 2:
    #         left, right, node.A, node.B, node.mid, c = self.half(S= S, F= F, p= p , rows= rows, cols= cols, above= above)
    #         if self.better(node.B, node.A):
    #             left,right,node.A,node.B = right,left,node.B,node.A
    #         node.left  = self.sway(S = S, F = F, p = p, rows = left, min = min,cols = cols, above = node.A)
            
    #     return node

    # def furthest(self, row1, rows=None, cols=None):
    #     t = self.around(row1, rows,cols)
    #     return t[-1][0]

# def row1(data, t):

#     if data["cols"]:
#         data["rows"].append(t)
#         temp = data["cols"]["x"]
#         temp.extend(data["cols"]["y"])
#         for cols in [data["cols"]["x"], data["cols"]["y"]]:
#             for col in cols:
#                 add(col, t[col['at']])
#     else:
#         data["cols"]= c.cols(t)
#     return data


# def rand(lo=0, hi=1):
#   Seed = 93716211
#   lo = lo or 0
#   hi = hi or 1
#   Seed = (16807 * Seed) % 2147483647
#   return lo + (hi - lo) * Seed / 2147483647


# def rint(lo=0, hi=1):
#   return math.floor(0.5 + rand(lo, hi))


# def add(col, x, n = 1):
#     if x != '?':
#         n = n or 1
#         col['n'] += n
#         if col['isSym']:
#             col['has'][x] = n + col['has'].get(x, 0)
#             if col['has'][x] > col['most']:
#                 col['most'], col['mode'] = col['has'][x], x
#         else:
#             col['lo'] = min(x, col['lo'])
#             col['hi'] = max(x, col['hi'])
#             all_ = len(col['has'])
#             pos = (all_ < 512 and all_+1) or (rand()< 512/col['n'] and rint(1, all_))
#             if pos:
                
#                 col['has'][pos-1] = x
#                 col['ok'] = False


# def adds(col, t):
#     for value in t or []:
#         add(col, value)
#     return col

# def extend(range, n, s):
#     range['lo'] = min(n, range['lo'])
#     range['hi'] = max(n, range['hi'])
#     add(range['y'], s)

# def cells(s):
#     t = []
#     for s1 in re.findall("[^,]+", s):
#         t.append(functions.coerce(s1))
#     return t

# def lines(sFilename, fun):
#     with open(sFilename, "r") as src:
#         for s in src:
#             s = s.rstrip("\r\n")
#             fun(s)
#     src.close()

# def CSV(sFilename, fun):
#     lines(sFilename, lambda line: fun(cells(line)))


## data functions!!
def new(src,rows):
    data = {"rows":[], "cols":None}
    add = function(t) 
    row(data,t)
    if type(src) == "string":
        csv(src,add)
    else:
        data['cols'] = c['src']['cols']['names']
    map(rows or {}, add)
    return data

# def read(sFile):
#     data = new()
#     callback = lambda t: row1(data, t)
#     CSV(sFile, callback)
#     return data

# def clone(data, ts = None, data1 = None):
#     # print(data)
#     data1 = row1(new(), data["cols"]["names"])
#     # print("ts", ts)
#     for t in (ts or []):
#         # print(t)
#         row1(data1, t)
#     return data1



