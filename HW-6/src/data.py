import math
import re
import sys

sys.path.append("../HW-6")
from str_func import *

from typing import Iterable
import functions
import row
import cols as c
import functions

import new_func


class DATA:

    def __init__(self, src, rows = None):
        self.rows = []
        self.cols = None
        add = lambda t: new_func.row(self, t)
        if isinstance(src, str):
            readCSV(src, add)
        else:
            self.cols = c.Cols(src.cols.names)
            if rows:
                for row in rows:
                    add(row)

    def read(self, sFile):
        data = DATA()
        callback = lambda t: new_func.row(data, t)
        readCSV(sFile, callback)
        return data

    def clone(self, data, ts = None):
        data1 = new_func.row(DATA(), data.cols.names)
        for t in (ts or []):
            new_func.row(data1, t)
        return data1


