import functions
import row
import cols
import math

class DATA:
    def __init__(self, src=None):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            for x in functions.csv_read(src):
                self.add(x)
        else:
            for x in src:
                self.add(x)

    def add(self, t):
        if self.cols:
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


    def dist(self, row1, row2, cols, n, d):
        n,d = 0,0
        if cols is not None:
            for col in cols:
                n =+1
                d =d + [col.dist(row1.cells[int(col.at)], row2.cells[int(col.at)])] ** the.p
            return (d/n)**(1/functions.the.p)

        elif cols.x is not None:
            for col in cols:
                n =+1
                d =d + [col.dist(row1.cells[int(col.at)], row2.cells[int(col.at)])] ** the.p
            return (d/n)**(1/the.p)

    def around(self):
        pass

    def half(self):
        pass

    def cluster(self):
        pass

    def sway(self):
        pass

