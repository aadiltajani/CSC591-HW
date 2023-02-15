import sys
sys.path.append("./src")
import functions
import NUM
import sym
import data
the = {'h': False, 'd': False, 's': 937162211, 'g': 'all', 'f': './etc/data/repgrid1.json', 'p': 2, 'F': .95, 'm': .5,'S': 512}
def test_the():
    if not functions.oo(the):
        print("❌ fail: eg")
    else:
        print("✅ pass: eg")

# def test_rand():
#     num1, num2 = NUM.NUM(), NUM.NUM()
#     tempSeed = the['s']
#     for i in range(1000):
#         tm, tempSeed = functions.rand(tempSeed, 0, 1)
#         num1.add(tm)
#     tempSeed = the['s']
#     for i in range(1000):
#         tm, tempSeed = functions.rand(tempSeed, 0, 1)
#         num2.add(tm)
#     m1, m2 = functions.rnd(num1.mid(), 10), functions.rnd(num2.mid(), 10)
#     temp = functions.rnd(m1, 1)
#     if m1 == m2 and 0.5 == functions.rnd(m1, 1):
#         print("✅ pass: rand")
#     else:
#         print("❌ fail: rand")


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

# def test_csv():
#     n = 0
#     t = functions.csv_read(r'./etc/data/auto93.csv')
#     n = n + len(t)
#     if n == 399:
#         print("✅ pass: csv")
        
#     else:
#        print("❌ fail: csv")

# def test_data():
#     Data = data.DATA(the['f'])
#     if len(Data.rows) != 398 and Data.cols.y[1].w != -1 and Data.cols.x[1].at != 1 and len(Data.cols.x) != 4:
#         print("❌ fail: data")
#     else:
#         print("✅ pass: data")
    
# def test_stats():
#      d = data.DATA(r'./etc/data/auto93.csv')
#      for k, cols in enumerate((d.cols.y, d.cols.x)):
#         print(k,"mid",functions.o(d.stats("mid",cols, 2)))
#         print("", "div",functions.o(d.stats("div",cols, 2)))

# def test_clone():
#     data1 = data.DATA(the['f'])
#     data2 = data1.clone(data1.rows)
#     if len(data1.rows) != len(data2.rows) and data1.cols.y[1].w != data2.cols.y[1].w and data1.cols.x[1].at != data2.cols.x[1].at and len(data1.cols.x) != len(data2.cols.x):
#         print("❌ fail: clone")
#     else:
#         print("✅ pass: clone")

# def test_around():
#     Data = data.DATA(the['f'])
#     for n,t in enumerate(Data.around(Data.rows[1], the['p'])):
#         if n%50 == 0:
#             print(n, '\t', functions.rnd(t['dist']), '\t', functions.o(t['row'].cells))
#     print("✅ pass: around")

# def test_half():
#     Data = data.DATA(the['f'])
#     left, right, A, B, mid, c = Data.half(S = the['S'],F =  the['F'], p = the['p'])
#     print(len(left), len(right), len(Data.rows))
#     print(functions.o(A.cells), c)
#     print(functions.o(mid.cells))
#     print(functions.o(B.cells))
#     print("✅ pass: half")

# def test_cluster():
#     Data = data.DATA(the['f'])
#     functions.show(Data.cluster(S = the['S'],F =  the['F'], p = the['p']),'mid',Data.cols.y,1)
#     print("✅ pass: cluster")

# def test_optimise():
#     Data = data.DATA(the['f'])
#     functions.show(Data.sway(S = the['S'],F =  the['F'], p = the['p']),'mid',Data.cols.y,1)
#     print("✅ pass: optimise")

def test_copy():
    t1 = {'a':1, 'b':{'c':2, 'd':[3]}}
    t2 = functions.copy(t1)
    t2['b']['d'][0] = 10000
    print("b4",functions.o(t1),"\nafter",functions.o(t2))
    print("✅ pass: eg")

def test_repcols():
    t = functions.repCols(functions.dofile(the['f']).get("cols"))
    for col in t.cols.all:
        print(vars(col))
    for row in t.rows:
        print(vars(row))
    print("✅ pass: repcols")

def test_synonyms():
    t = functions.dofile(the['f'])["cols"]
    cols = functions.repCols(t)
    x = cols.cluster()
    functions.show(x)
    # functions.show(functions.repCols(functions.dofile(the['f']).get("cols")).cluster())
    print("✅ pass: synonyms")

def test_reprows():
    t = functions.dofile(the['f'])
    rows = functions.repRows(t, functions.transpose(t['cols']))
    functions.map(rows.cols.all, functions.oo)
    functions.map(rows.rows, functions.oo)
    print("✅ pass: reprows")

def test_prototypes():
    t = functions.dofile(the['f'])
    
    rows = functions.repRows(t, functions.transpose(t["cols"]))
    functions.show(rows.cluster())
    print("✅ pass: prototypes")

def test_position():
    t = functions.dofile(the['f'])
    rows = functions.repRows(t, functions.transpose(t["cols"]))
    rows.cluster()
    functions.repPlace(rows)
    print("✅ pass: position")

def test_repgrid():
    t = functions.dofile(the['f'])
    rows = functions.repRows(t, functions.transpose(t["cols"]))
    cols = functions.repCols(t["cols"])
    functions.show(rows.cluster())
    functions.show(cols.cluster())
    functions.repPlace(rows)
    print("✅ pass: repgrid")

test_the()
# test_rand()
test_sym()
test_num()
# test_csv()
# test_data()
# test_stats()
# test_clone()
# test_around()
# test_half()
# test_cluster()
# test_optimise()
test_copy()
test_repcols()
test_synonyms()
test_reprows()
test_prototypes()
test_position()
test_repgrid()