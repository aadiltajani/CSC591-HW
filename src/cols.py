import sys
sys.path.append("./code")
from num import Num
from SYM import Sym

class Cols:

    def __init__(self,names):
        self.names=names
        self.all=[]
        self.x=[]
        self.y=[]
        self.klass=None
        
        for column_name in self.names:
            if column_name[0].isupper():
                column=Num(names.index(column_name),column_name)
            else:
                column=Sym(names.index(column_name),column_name)
            
            if column_name[-1]!=':':
                if('!' in column_name or '+' in column_name or '-' in column_name):
                    self.y.append(column)
                else:
                    self.x.append(column)

            if column_name[-1]=='!':
                self.klass=column
            self.all.append(column)
    
