import random
import sys


sys.path.append('../HW-6/')

import getopt
import functions
import NUM
import SYM
import data
import sys
import discretization
from functions import *
from list_func import *
from str_func import *
from query import *
from functions import *
from new_func import *
from optimization import *
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


# def rand():
#     num1, num2 = NUM(), NUM()
#     Seed=the['seed']
#     for i in range(1, 1000):
#         num1.add(rand(0, 1))
#     Seed=the['seed']
#     for i in range(1, 1000):
#         num2.add(rand(0, 1))
#     m1 = rnd(num1.mid(), 10)
#     m2 = rnd(num2.mid(), 10)
#     return m1==m2 and .5 == rnd(m1,1)


if n > 0:
    args, vals = getopt.getopt(cli_list, shorts, longs)
    for arg, val in args:
        if arg == '-b' or arg == '--bins':
            the['b'] = val
        elif arg == '-g' or arg == '--go':
            the['g'] = val
        elif arg == '-h' or arg == '--help':
            the['h'] = True
        elif arg == '-s' or arg == '--seed':
            the['s'] = val
        elif arg == '-f' or arg == '--file':
            the['f'] = val
        elif arg == '-F' or arg == '--Far':
            the['F'] = val
        elif arg == '-m' or arg == '--min':
            the['m'] = val
        elif arg == '-p' or arg == '--p':
            the['p'] = val
        elif arg == '-c' or arg == '--cliffs':
            the['H'] = val
        elif arg == '-H' or arg == '--Halves':
            the['H'] = val
        elif arg == '-M' or arg == '--Max':
            the['M'] = val
        elif arg == '-r' or arg == '--rest':
            the['r'] = val
        elif arg == '-R' or arg == '--Reuse':
            the['R'] = val
if the['h']:
    print(help)
else:
    if the['g'] == 'all' or the['g'] == 'the':
        if not oo(the):
            print("❌ fail: the")
        else:
            print("✅ pass: the")


    if the['g'] == 'all' or the['g'] == 'rand':
        Seed, t, u = the['s'], [], []
        for i in range(0,1000):
            t.append(rint(100))
            u.append(rint(100))
        for i in range(len(t)):
            assert(t[i]==u[i])
        print("✅ pass: rand")

    if the['g'] == 'all' or the['g'] == 'some':
        max = 32
        num1 = NUM.Num()
        for i in range(1,10000):
            add(num1,i)
        oo(has(num1))



    # if the['g'] == 'all' or the['g'] == 'syms':
    #     sym = adds(SYM.SYM(), ["a","a","a","a","b","b","c"])
    #     print(mid(sym), rnd(div(sym)))
    #     if 1.38 != rnd(div(sym),2):
    #         print("❌ fail: sym")
    #     else:
    #         print("✅ pass: sym")


    if the['g'] == 'all' or the['g'] == 'nums':
        num1, num2 = NUM.Num(), NUM.Num()
        for i in range(10000):
            add(num1, rand())
            add(num2, rand()**2)
        print(1, rnd(mid(num1),1), rnd(div(num1)))
        print(2, rnd(mid(num2),1), rnd(div(num2))) 
        if .5 == rnd(mid(num1),1) and mid(num1)> mid(num2):
            print("✅ pass: num")
        else:
            print("❌ fail: num")            

    if the['g'] == 'all' or the['g'] == 'csv':
        n = 0
        t = csv_read(the['f'])
        for i in t:
            n+=len(i)
        if 3192 != n:
            print("❌ fail: sym")
        else:
            print("✅ pass: sym")

    if the['g'] == 'all' or the['g'] == 'data':
        d = data.DATA(the['f'])
        col = d.cols.x[1].col
        print(col.lo, col.hi, mid(col), div(col))
        oo(stats(d))
        print("✅ pass: data")

    if the['g'] == 'all' or the['g'] == 'clone':
        data1 = data.DATA(the['f'])
        data2 = data.DATA(data1, data1.rows)
        oo(stats(data1))
        oo(stats(data2))
        print("✅ pass: clone")


    if the['g'] == 'all' or the['g'] == 'cliffs':
        assert cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]) == False, "1"
        assert cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]) == True, "2"
        t1 = []
        t2 = []
        for i in range(0, 1000):
            t1.append(random.random())
            t2.append(random.random() ** 0.5)
        assert cliffsDelta(t1, t1) == False, "3"
        assert cliffsDelta(t1, t2) == True, "4"
        diff = False
        j = 1.0
        while not diff:
            t3 = list(map(lambda x: x*j, t1))
            diff = cliffsDelta(t1, t3)
            print(">", round(j, 4), diff)
            j *= 1.025      
        print("✅ pass: cliffs")


    if the['g'] == 'all' or the['g'] == 'dist':
        d = data.DATA(the['f'])

        num = NUM.Num()
        for row in d.rows:
            add(num, dist(d, row, d.rows[0]))
        oo({
            'lo': num.lo,
            'hi': num.hi,
            'mid': rnd(mid(num)),
            'div': rnd(div(num))
                      })
        print("✅ pass: dist")
        
    if the['g'] == 'all' or the['g'] == 'tree':
        d = data.DATA(the['f'])

        showTree(tree(d))
        print("✅ pass: tree")


    # if the['g'] == 'all' or the['g'] == 'sway':
    #     d = data.read(the['f'])
    #     best, rest = sway(d)
    #     print("\nall ", o(stats(d))) 
    #     print("    ",   o(stats(d,div))) 
    #     print("\nbest", o(stats(best))) 
    #     print("    ",   o(stats(best,div))) 
    #     print("\nrest", o(stats(rest))) 
    #     print("    ",   o(stats(rest,div))) 
    #     print("\nall ~= best?", o(diffs(best['cols']['y'], d['cols']['y'])))
    #     print("best ~= rest?", o(diffs(best['cols']['y'], rest['cols']['y'])))
    #     print("✅ pass: sway")


    # if the['g'] == 'all' or the['g'] == 'bins':
    #     d = data.read(the['f'])
    #     best,rest = sway(d)
    #     print("all","","","",o({'best': len(best['rows']), 'rest': len(rest['rows'])}))
    #     for k,t in enumerate(discretization.bins(d['cols']['x'],{'best':best['rows'], 'rest':rest['rows']})):
    #         for _,range in enumerate(t):
    #             b4 = range['txt']
    #             print(range['txt'],range['lo'],range['hi'],
    #             rnd(value(range['y']['has'], len(best['rows']),len(rest['rows']),"best")), 
    #             o(range['y']['has']))
    #     print("✅ pass: bins")


    if the['g'] == 'all' or the['g'] == 'xpln':
        d = data.DATA(the['f'])
        best,rest,evals = sway(d)
        rule,most= discretization.xpln(d,best,rest)
        print("\n-----------\nexplain=", d.showRule(rule))
        selects = discretization.selects(rule,d.rows)
        data_selects = [s for s in selects if s!=None]
        data1= d.clone(data_selects)
        print("all               ",d.stats('mid', d.cols.y, 2),d.stats('div', d.cols.y, 2))
        print("sway with",evals,"evals",best.stats('mid', best.cols.y, 2),best.stats('div', best.cols.y, 2))
        print("xpln on",evals,"evals",data1.stats('mid', data1.cols.y, 2),data1.stats('div', data1.cols.y, 2))
        top,_ = d.betters(len(best.rows))
        top = d.clone(top)
        print("sort with",len(d.rows),"evals",top.stats('mid', top.cols.y, 2),top.stats('div', top.cols.y, 2))
