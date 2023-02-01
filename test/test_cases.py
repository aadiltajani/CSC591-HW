import sys
sys.path.append("./src")
import functions
import NUM
import sym
import data
the = {'h': False, 'd': False, 's': 937162211, 'g': 'all', 'f': './etc/data/auto93.csv'}

def test_the():
    if not functions.oo(the):
        print("❌ fail: eg")
    else:
        print("✅ pass: eg")

def test_rand():
    num1, num2 = NUM.NUM(), NUM.NUM()
    tempSeed = the['s']
    for i in range(1000):
        tm, tempSeed = functions.rand(tempSeed, 0, 1)
        num1.add(tm)
    tempSeed = the['s']
    for i in range(1000):
        tm, tempSeed = functions.rand(tempSeed, 0, 1)
        num2.add(tm)
    m1, m2 = functions.rnd(num1.mid(), 10), functions.rnd(num2.mid(), 10)
    temp = functions.rnd(m1, 1)
    if m1 == m2 and 0.5 == functions.rnd(m1, 1):
        print("✅ pass: rand")
    else:
        print("❌ fail: rand")


def test_sym():
    Sym = sym.sym()
    for i in ["a", "a", "a", "a", "b", "b", "c"]:
        Sym.add(i)
    val = 'a' == Sym.mid() and 1.379 == functions.rnd(Sym.div())
    if not val:
        print("❌ fail: sym")
    else:
        print("✅ pass: sym")

def test_num():
    num = NUM.NUM()
    for i in [1, 1, 1, 1, 2, 2, 3]:
        num.add(i)
    val = 11/7 == num.mid() and 0.787 == functions.rnd(num.div())
    if not val:
        print("❌ fail: num")
    else:
        print("✅ pass: num")

def test_csv():
    n = 0
    t = functions.csv_read(r'./etc/data/auto93.csv')
    n = n + len(t)
    if n == 399:
        print("✅ pass: csv")
        
    else:
       print("❌ fail: csv")

def test_data():
    Data = data.DATA(the['f'])
    if len(Data.rows) != 398 and Data.cols.y[1].w != -1 and Data.cols.x[1].at != 1 and len(Data.cols.x) != 4:
        print("❌ fail: data")
    else:
        print("✅ pass: data")
    
def test_stats():
     d = data.DATA(r'./etc/data/auto93.csv')
     for k, cols in enumerate((d.cols.y, d.cols.x)):
        print(k,"mid",functions.o(d.stats("mid",cols, 2)))
        print("", "div",functions.o(d.stats("div",cols, 2)))

test_the()
test_rand()
test_sym()
test_num()
test_csv()
test_data()
test_stats()