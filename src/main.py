import sys
import getopt
import functions
import NUM
import sym
import data
import sys

sys.path.append("./src")
n = len(sys.argv)
cli_list = sys.argv[1:]
shorts = 'dg:hs:f:F:m:p:S:'
longs = ['dump', 'go=', 'help', 'seed=', 'file=', 'Far=', 'min=', 'p=', 'Sample=']
the = {'h': False, 'd': False, 's': 937162211, 'g': 'all', 'f': './etc/data/repgrid1.json', 'p': 2, 'F': .95, 'm': .5,
       'S': 512}
help = """script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../etc/data/auto93.csv
  -F  --Far     distance to "faraway"  = .95
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -m  --min     stop clusters at N^min = .5
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
  -S  --Sample  sampling data size     = 512
ACTIONS:
"""


def rand():
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
    return m1 == m2 and 0.5 == functions.rnd(m1, 1)


if n > 0:
    args, vals = getopt.getopt(cli_list, shorts, longs)
    for arg, val in args:
        if arg == '-d' or arg == '--dump':
            the['d'] = True
        elif arg == '-g' or arg == '--go':
            the['g'] = val
        elif arg == '-h' or arg == '--help':
            the['h'] = True
        elif arg == '-s' or arg == '--seed':
            the['s'] = val
        elif arg == '-f' or arg == '--file':
            the['f'] = val
        # elif arg == '-F' or arg == '--Far':
        #     the['F'] = val
        # elif arg == '-m' or arg == '--min':
        #     the['m'] = val
        elif arg == '-p' or arg == '--p':
            the['p'] = val
        # elif arg == '-S' or arg == '--Sample':
        #     the['S'] = val
if the['h']:
    print(help)
else:
    if the['g'] == 'all' or the['g'] == 'the':
        if not functions.oo(the):
            print("❌ fail: the")
        else:
            print("✅ pass: the")


    # if the['g'] == 'all' or the['g'] == 'rand':
    #     if not rand():
    #         print("❌ fail: rand")
    #     else:
    #         print("✅ pass: rand")


    if the['g'] == 'all' or the['g'] == 'sym':
        Sym = sym.sym()
        for i in ["a", "a", "a", "a", "b", "b", "c"]:
            Sym.add(i)
        val = 'a' == Sym.mid() and 1.379 == functions.rnd(Sym.div())
        if not val:
            print("❌ fail: sym")
        else:
            print("✅ pass: sym")


    if the['g'] == 'all' or the['g'] == 'num':
        num = NUM.NUM()
        for i in [1, 1, 1, 1, 2, 2, 3]:
            num.add(i)
        val = 11 / 7 == num.mid() and 0.787 == functions.rnd(num.div())
        if not val:
            print("❌ fail: num")
        else:
            print("✅ pass: num")


    if the['g'] == 'all' or the['g'] == 'copy':
        t1 = {'a':1, 'b':{'c':2, 'd':[3]}}
        t2 = functions.copy(t1)
        t2['b']['d'][0] = 10000
        print("b4",functions.o(t1),"\nafter",functions.o(t2))
        print("✅ pass: copy")


    if the['g'] == 'all' or the['g'] == 'repcols':
        t = functions.repCols(functions.dofile(the['f']).get("cols"))
        functions.map(t.cols.all, functions.oo)
        functions.map(t.rows, functions.oo)
        print("✅ pass: repcols")


    if the['g'] == 'all' or the['g'] == 'synonyms':
        t = functions.repCols(functions.dofile(the['f']).get("cols"))
        x = t.cluster(S = the['S'],F =  the['F'], p = the['p'])
        functions.show(x, 3)
        # functions.show(functions.repCols(functions.dofile(the['f']).get("cols")).cluster())
        print("✅ pass: synonyms")

        
    if the['g'] == 'all' or the['g'] == 'reprows':
        t = functions.dofile(the['f'])
        rows = functions.repRows(t, functions.transpose(t['cols']))
        functions.map(rows.cols.all, functions.oo)
        functions.map(rows.rows, functions.oo)
        print("✅ pass: reprows")




    # if the['g'] == 'all' or the['g'] == 'csv':
    #     n = functions.csv_read(the['f'])
    #     if len([i for sublist in n for i in sublist]) != 8 * 399:
    #         print("❌ fail: csv")
    #     else:
    #         print("✅ pass: csv")
    # if the['g'] == 'all' or the['g'] == 'data':
    #     Data = data.DATA(the['f'])
    #     if len(Data.rows) != 398 and Data.cols.y[1].w != -1 and Data.cols.x[1].at != 1 and len(Data.cols.x) != 4:
    #         print("❌ fail: data")
    #     else:
    #         print("✅ pass: data")
    # if the['g'] == 'all' or the['g'] == 'stats':
    #     Data = data.DATA(the['f'])
    #     try:
    #         for k, cols in ([('y', Data.cols.y), ('x', Data.cols.x)]):
    #             print(k, "mid", functions.o(Data.stats("mid", cols, 2)))
    #             print(" ", "div", functions.o(Data.stats("div", cols, 2)))
    #         print("✅ pass: stats")
    #     except Exception as e:
    #         print(e, "❌ fail: stats")
    # if the['g'] == 'all' or the['g'] == 'clone':
    #         data1 = data.DATA(the['f'])
    #         data2 = data1.clone(data1.rows)
    #         if len(data1.rows) != len(data2.rows) and data1.cols.y[1].w != data2.cols.y[1].w and data1.cols.x[1].at != data2.cols.x[1].at and len(data1.cols.x) != len(data2.cols.x):
    #             print("❌ fail: clone")
    #         else:
    #             print("✅ pass: clone")
    # if the['g'] == 'all' or the['g'] == 'around':
    #         Data = data.DATA(the['f'])
    #         for n,t in enumerate(Data.around(Data.rows[1], the['p'])):
    #             if n%50 == 0:
    #                 print(n, '\t', functions.rnd(t['dist']), '\t', functions.o(t['row'].cells))
    #         print("✅ pass: around")
    # if the['g'] == 'all' or the['g'] == 'half':
    #             Data = data.DATA(the['f'])
    #             left, right, A, B, mid, c = Data.half(S = the['S'],F =  the['F'], p = the['p'])
    #             print(len(left), len(right), len(Data.rows))
    #             print(functions.o(A.cells), c)
    #             print(functions.o(mid.cells))
    #             print(functions.o(B.cells))
    #             print("✅ pass: half")
    # if the['g'] == 'all' or the['g'] == 'cluster':
    #             Data = data.DATA(the['f'])
    #             functions.show(Data.cluster(S = the['S'],F =  the['F'], p = the['p']),'mid',Data.cols.y,1)
    #             print("✅ pass: cluster")
    # if the['g'] == 'all' or the['g'] == 'optimise':
    #             Data = data.DATA(the['f'])
    #             functions.show(Data.sway(S = the['S'],F =  the['F'], p = the['p']),'mid',Data.cols.y,1)
    #             print("✅ pass: optimise")