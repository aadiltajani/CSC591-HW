import sys
# sys.path.append("./code")
from NUM import NUM
from sym import sym
from row import Row


class Cols:

    def __init__(self, names):
        self.names = names
        self.all = []
        self.x = []
        self.y = []
        self.klass = None

        for k, column_name in enumerate(self.names):
            if column_name[0].isupper():
                column = NUM(k, column_name)
            else:
                column = sym(k, column_name)
            self.all.append(column)
            if column_name[-1] != 'X':
                self.klass = column_name
                if '+' == column_name[-1] or '-' == column_name[-1]:
                    self.y.append(column)
                else:
                    self.x.append(column)

            # if column_name[-1] == '!':
            #     self.klass = column
            # self.all.append(column)

    def add(self, row):
        for t in [self.x, self.y]:
            for col in t:
                col.add(row.cells[int(col.at)])
