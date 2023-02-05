import functions
import row
import cols
import math
import random

class DATA:
    def __init__(self, src=None):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            for x in functions.csv_read(src):
                self.add(x)
        else:
            self.add(src)

    def add(self, t):
        if self.cols:
            if isinstance(t, list):
                t = row.Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = cols.Cols(t)

    def clone(self, init=None):
        data = DATA(self.cols.names)
        for x in init or []:
            data.add(x)
        return data

    def stats(self, what=None, cols=None, nPlaces=None):
        def fun(col):
            x = col.mid() if what == 'mid' else col.div()
            return col.rnd(x, nPlaces)

        return {col.txt: fun(col) for col in cols}

    def better(self, row1, row2, s1, s2, ys, x, y):
        s1, s2 = 0,0
        for col in ys:
            self.x = col.norm(row1.cells[int(col.at)])
            self.y = col.norm(row2.cells[int(col.at)])
            s1 = s1 - math.exp(col.w * (x - y)/len(ys))
            s2 = s2 - math.exp(col.w * (y - x)/len(ys))
        if s1/len(ys) < s2/len(ys):
            return True
        else:
            return False


    def dist(self, row1, row2, p, cols=None):
        n,d = 0,0
        cols = self.cols if cols is None else cols
        for col in cols.x:
            n =+1
            d =d + (col.dist(row1.cells[int(col.at)], row2.cells[int(col.at)])) ** p
        return (d/n)**(1/p)

    def around(self, row1, p, rows=None):
        rows = self.rows if rows is None else rows
        return sorted(
            [{'row': row2, 'dist': self.dist(row1, row2, p, self.cols)} for row2 in rows], key=lambda x:x['dist']
        )

    def half(self, S, F, p):
        mid = None
        rows = self.rows
        some = random.choices(rows, k=S)
        A = random.choice(some)
        B = self.around(A, p, some)[int(F*len(rows))]['row']
        c = self.dist(A, B,p)
        def project(row): 
            return {'row': row, 'dist': functions.cosine(self.dist(row,A,p), self.dist(row, B,p), c)}
        left, right = [], []
        for n, tmp in enumerate(sorted(map(project, rows), key=lambda x:x['dist'])):
            if n <= len(rows)//2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A, B, mid, c



    def cluster(self):
        pass

    def sway(self):
        pass

