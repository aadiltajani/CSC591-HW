import random
import sys
sys.path.append('./src')

import getopt
import functions
import NUM
import SYM
import data
import sys
import discretization


n = len(sys.argv)
cli_list = sys.argv[1:]
shorts = 'b:c:f:F:g:h:H:m:M:p:r:R:s:'
longs = ['bins=', 'cliffs=', 'file=', 'Far=', 'go=', 'help=', 'Halves=', 'min=', 'Max=', 'p=', 'rest=', 'Reuse=', 'seed=']
the = {'b':16, 'c':0.147, 'f': './etc/data/auto93.csv', 'g': 'all', 'h': False, 'H': 512, 'm':0.5, 'M':512, 'r':4, 'R':True, 's': 937162211, 'p': 2}
help = """script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -b  --bins    initial number of bins       = 16
  -c  --cliffs  cliff's delta threshold      = .147
  -f  --file    data file                    = ../etc/data/auto93.csv
  -F  --Far     distance to distant          = .95
  -g  --go      start-up action              = nothing
  -h  --help    show help                    = false
  -H  --Halves  search space for clustering  = 512
  -m  --min     size of smallest cluster     = .5
  -M  --Max     numbers                      = 512
  -p  --p       dist coefficient             = 2
  -r  --rest    how many of rest to sample   = 4
  -R  --Reuse   child splits reuse a parent pole = true
  -s  --seed    random number seed           = 937162211
ACTIONS:
"""

def test_rand():
    Seed, t, u = 1, [], []
    for i in range(0,1000):
        t.append(functions.rint(0,100,Seed))
        u.append(functions.rint(0,100,Seed))
    for i in range(len(t)):
        assert(t[i]==u[i])
    print("✅ pass: rand")


def test_sym():
    sym = functions.adds(SYM.SYM(), ["a","a","a","a","b","b","c"])
    print(functions.mid(sym), functions.rnd(functions.div(sym)))
    if 1.38 != functions.rnd(functions.div(sym),2):
        print("❌ fail: sym")
    else:
        print("✅ pass: sym")

def test_nums():
    num1, num2 = NUM.num(), NUM.num()
    for i in range(10000):
        functions.add(num1, functions.rand())
        functions.add(num2, functions.rand()**2)
    print(1, functions.rnd(functions.mid(num1),1), functions.rnd(functions.div(num1)))
    print(2, functions.rnd(functions.mid(num2),1), functions.rnd(functions.div(num2))) 
    if .5 == functions.rnd(functions.mid(num1),1) and functions.mid(num1)> functions.mid(num2):
        print("✅ pass: num")
    else:
        print("❌ fail: num") 

def test_csv():
    n = 0
    t = functions.csv_read(the['f'])
    for i in t:
        n+=len(i)
    if 3192 != n:
        print("❌ fail: sym")
    else:
        print("✅ pass: sym")


def test_data():
    d = data.read(the['f'])
    col = d["cols"]["x"][0]
    print(col['lo'], col['hi'], functions.mid(col), functions.div(col))
    functions.oo(functions.stats(d))
    print("✅ pass: data")


def test_clone():
    data1 = data.read(the['f'])
    data2= data.clone(data1, data1['rows'])
    functions.oo(functions.stats(data1))
    functions.oo(functions.stats(data2))
    print("✅ pass: clone")

def test_cliffs():
    assert functions.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]) == False, "1"
    assert functions.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]) == True, "2"
    t1 = []
    t2 = []
    for i in range(0, 1000):
        t1.append(random.random())
        t2.append(random.random() ** 0.5)
    assert functions.cliffsDelta(t1, t1) == False, "3"
    assert functions.cliffsDelta(t1, t2) == True, "4"
    diff = False
    j = 1.0
    while not diff:
        t3 = list(map(lambda x: x*j, t1))
        diff = functions.cliffsDelta(t1, t3)
        print(">", round(j, 4), diff)
        j *= 1.025      
    print("✅ pass: cliffs")

def test_dist():
    d = data.read(the['f'])
    num = NUM.num()
    for row in d['rows']:
        functions.add(num, functions.dist(d, row, d['rows'][0]))
    functions.oo({
        'lo': num['lo'],
        'hi': num['hi'],
        'mid': functions.rnd(functions.mid(num)),
        'div': functions.rnd(functions.div(num))
                    })
    print("✅ pass: dist")

def test_tree():
    functions.showTree(functions.tree(data.read(the['f'])))
    print("✅ pass: tree")


def test_sway():
    d = data.read(the['f'])
    best, rest = functions.sway(d)
    print("\nall ", functions.o(functions.stats(d))) 
    print("    ",   functions.o(functions.stats(d,functions.div))) 
    print("\nbest", functions.o(functions.stats(best))) 
    print("    ",   functions.o(functions.stats(best,functions.div))) 
    print("\nrest", functions.o(functions.stats(rest))) 
    print("    ",   functions.o(functions.stats(rest,functions.div))) 
    print("\nall ~= best?", functions.o(functions.diffs(best['cols']['y'], d['cols']['y'])))
    print("best ~= rest?", functions.o(functions.diffs(best['cols']['y'], rest['cols']['y'])))
    print("✅ pass: sway")


def test_bins():
    d = data.read(the['f'])
    best,rest = functions.sway(d)
    print("all","","","",functions.o({'best': len(best['rows']), 'rest': len(rest['rows'])}))
    for k,t in enumerate(discretization.bins(d['cols']['x'],{'best':best['rows'], 'rest':rest['rows']})):
        for _,range in enumerate(t):
            b4 = range['txt']
            print(range['txt'],range['lo'],range['hi'],
            functions.rnd(functions.value(range['y']['has'], len(best['rows']),len(rest['rows']),"best")), 
            functions.o(range['y']['has']))
    print("✅ pass: bins")



test_rand()
test_sym()
test_nums()
test_csv()
test_data()
test_clone()
test_cliffs()
test_dist()
test_tree()
test_sway()
test_bins()