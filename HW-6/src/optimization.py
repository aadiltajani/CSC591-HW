from functions import *
from data import DATA
from cluster import *

def sway(data):

    def worker(rows, worse, evals0, above = None):
        if len(rows) <= len(data.rows) ** 0.5:
            return rows, many(worse, 4*len(rows)), evals0
        else:
            l , r, A, B, c, evals = half(data, rows, None, above)
            if better(data, B, A):
                l, r, A, B = r, l, B, A
            for row in r:
                worse.append(row)
            return worker(l, worse, evals + evals0, A)
    best, rest, evals = worker(data.rows, [], 0)
    return DATA(data, best), DATA(data, rest), evals