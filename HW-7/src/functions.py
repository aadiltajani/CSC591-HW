import math
import sys
from copy import deepcopy
import NUM
import stats
sys.path.append("./HW-7/src")


def mid(col):
    pass

def div(col):
    pass

def cliffsDelta(ns1, ns2): 
    n, gt, lt = 0, 0, 0 
    if len(ns1) > 128: 
        ns1 = stats.samples(ns1, 128)
    if len(ns2) > 128: 
        ns2 = stats.samples(ns2, 128)
    for x in ns1:
        for y in ns2: 
            n = n + 1 
            if x > y: 
                gt += 1
            if x < y: 
                lt += 1
    return abs(lt - gt) / n <= 0.4
