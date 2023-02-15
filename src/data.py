from pyparsing import Iterable
import functions
import row
import cols


class DATA:
    def __init__(self, src=None):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            for x in functions.csv_read(src):
                self.add(x)
        else:
            # self.add(src)
            functions.map(src, self.add)

    def add(self, t):
        if self.cols:
            t = t if hasattr(t, "cells") else row.Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = cols.Cols(t)

    def clone(self, init=None):
        data = DATA([self.cols.names])
        if(type(init) == dict):
            for i, item in init.items():
                data.add(item.cells)
            return data
        else:
            for row in init:
                data.add(row)
            return data
        

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


    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        for _, col in enumerate(self.cols.x or cols):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** 2
        return (d / n) ** (1 / 2)

    def around(self, row1, rows=None, cols=None):
        if rows is None:
            rows = self.rows
        if isinstance(rows, Iterable):
            iterable = rows
        else:
            iterable = self.rows
        rows_with_distance = [(row2, self.dist(row1, row2, cols))
                              for row2 in iterable]
        sorted_rows = sorted(rows_with_distance, key=lambda x: x[1])
        return [(row, dist) for row, dist in sorted_rows]

    def half(self, rows = None, cols = None, above = None):
        A, B, c, mid = None, None, None, None
        
        def project(row): 
            x, y = functions.cosine(dist(row,A), dist(row, B), c)
            row.x = x or row.x
            row.y = y or row.y
            return {'row': row, 'x':x, 'y':y }

        def dist(row1, row2, cols=None):
            return self.dist(row1, row2, cols)

        rows = rows or self.rows
        A = functions.any(rows)
        B = self.furthest(A, rows)
        c = dist(A, B)

        left, right = [], []
        mapVAR = [project(row) for row in rows]
        sorted_rows = sorted(mapVAR, key=lambda x: x["x"])
        for n, tmp in enumerate(sorted_rows):
            if n <= len(rows) // 2 - 1:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c
        

    def cluster(self, rows = None, cols = None, above = None):
        rows = rows if rows != None else self.rows
        cols = cols if cols != None else self.cols.x
        node = {'data': self.clone(rows)}

        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'] = self.half(rows= rows, cols= cols, above= above)
            node['left']  = self.cluster(rows = left, cols = cols, above = node['A'])
            node['right'] = self.cluster(rows = right, cols = cols, above = node['B'])
        return node

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

    def furthest(self, row1, rows=None, cols=None):
        t = self.around(row1,rows, cols)
        return t[-1][0]

