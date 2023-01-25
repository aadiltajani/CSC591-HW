import sys
sys.path.append("./code")
from NUM import NUM
from SYM import sym
from row import Row

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

    def add(self,row):
        for _,names in enumerate(zip(self.x,self.y)):
            for i,col in enumerate(names):
                col.add(row.cells[i])


    
