import functions
import math

def bins(cols, rowss, the):
    out = []
    for col in cols:
        ranges = []
        for y, rows in enumerate(rowss):
            for row in rows:
                x,k = row[col['at']]
                if x != '?':
                    k = bin(col, x, the)
                    ranges[k] = ranges[k] or functions.range(col['at'], col['txt'], x)
                    functions.extend(ranges[k], x, y)
        ranges = sorted(functions.map(ranges, functions.itself))
        out[len(out)] = ranges if col['isSym'] else mergeAny(ranges)
    return out

def bin(col, x, the):
    if x == '?' or col['isSym']:
        return x
    tmp = (col['hi'] - col['lo'] / (the['b'] - 1))
    return 1 if col['hi'] == col['lo'] else math.floor(x/tmp + 0.5)*tmp

def noGaps(t):
    for j in range(1, len(t)):
        t[j].lo = t[j-1].hi
        t[1].lo = - math.inf
        t[len(t) - 1].hi = math.inf
    return t

def mergeAny(ranges0):
    ranges1, j, left, right, y = [], 1, None, None, None
    while j <= len(ranges0) - 1:
        left, right = ranges0[j], ranges0[j+1]
        if right:
            y = merge2(left.y, right.y)
            if y:
                j += 1
                left['hi'], left['y'] = right['hi'], y
        ranges1.append(left)
        j += 1
    return noGaps(ranges0) if len(ranges0) == len(ranges1) else mergeAny(ranges1)

def merge2(col1, col2):
    new = merge(col1, col2)
    if functions.div(new) <= (functions.div(col1)*col1['n'] + functions.div(col2)*col2['n']) / new['n']:
        return new

def merge(col1, col2):
    new = merge(col1, col2)
    if col1['isSym']:
        for x,n in enumerate(col2['has']):
            functions.add(new, x, n)
    else:
        for n in col2['has']:
            functions.add(new, n)
        new['lo'] = min(col1['lo'], col2['lo'])
        new['hi'] = max(col1['hi'], col2['hi'])
    return new