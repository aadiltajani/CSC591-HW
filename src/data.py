
class DATA:
    def __init__(self, src=None, fun=None):
        self.rows = []
        self.cols = None
        if fun is None:
            def fun(x):
                self.add(x)
        if isinstance(src, str):
            csv(src, fun)
        else:
            for x in src or []:
                fun(x)

    def add(self, t):
        if self.cols:
            t = t.cells if hasattr(t, "cells") else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)

    def clone(self, init=None):
        data = DATA(self.cols.names)
        for x in init or []:
            data.add(x)
        return data

    def stats(self, what=None, cols=None, nPlaces=None):
        def fun(k, col):
            return round(getattr(col, what or "mid")(col), nPlaces), col.txt
        return {k: fun(k, col) for k, col in (cols or self.cols.y).items()}
