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
