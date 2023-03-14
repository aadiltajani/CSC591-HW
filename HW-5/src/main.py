import random
import sys
import getopt
import functions
import NUM
import SYM
import data
import sys
import discretization
sys.path.append("./src")
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
#         num1.add(functions.rand(0, 1))
#     Seed=the['seed']
#     for i in range(1, 1000):
#         num2.add(functions.rand(0, 1))
#     m1 = functions.rnd(num1.mid(), 10)
#     m2 = functions.rnd(num2.mid(), 10)
#     return m1==m2 and .5 == functions.rnd(m1,1)


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
        if not functions.oo(the):
            print("❌ fail: the")
        else:
            print("✅ pass: the")


    if the['g'] == 'all' or the['g'] == 'rand':
        Seed, t, u = 1, [], []
        for i in range(0,1000):
            t.append(functions.rint(0,100,Seed))
            u.append(functions.rint(0,100,Seed))
        for i in range(len(t)):
            assert(t[i]==u[i])
        print("✅ pass: rand")


    if the['g'] == 'all' or the['g'] == 'syms':
        sym = functions.adds(SYM.SYM(), ["a","a","a","a","b","b","c"])
        print(functions.mid(sym), functions.rnd(functions.div(sym)))
        if 1.38 != functions.rnd(functions.div(sym),2):
            print("❌ fail: sym")
        else:
            print("✅ pass: sym")


    if the['g'] == 'all' or the['g'] == 'nums':
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

    if the['g'] == 'all' or the['g'] == 'csv':
        n = 0
        t = functions.csv_read(the['f'])
        for i in t:
            n+=len(i)
        if 3192 != n:
            print("❌ fail: sym")
        else:
            print("✅ pass: sym")

    if the['g'] == 'all' or the['g'] == 'data':
        d = data.read(the['f'])
        col = d["cols"]["x"][0]
        print(col['lo'], col['hi'], functions.mid(col), functions.div(col))
        functions.oo(functions.stats(d))

    if the['g'] == 'all' or the['g'] == 'clone':
        data1 = data.read(the['f'])
        data2= data.clone(data1, data1['rows'])
        functions.oo(functions.stats(data1))
        functions.oo(functions.stats(data2))


    if the['g'] == 'all' or the['g'] == 'cliffs':
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


    if the['g'] == 'all' or the['g'] == 'dist':
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
        
    if the['g'] == 'all' or the['g'] == 'tree':
        functions.showTree(functions.tree(data.read(the['f'])))


    if the['g'] == 'all' or the['g'] == 'sway':
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


    if the['g'] == 'all' or the['g'] == 'bins':
        d = data.read(the['f'])
        best,rest = functions.sway(d)
        print("all","","","",functions.o({'best': len(best['rows']), 'rest': len(rest['rows'])}))
        for k,t in discretization.bins(d['cols']['x'],{'best':best['rows'], 'rest':rest['rows']}):
            for _,range in enumerate(t):
                b4 = range['txt']
                print(range['txt'],range['lo'],range['hi'],
                functions.rnd(functions.value(range['y']['has'], len(best['rows']),len(rest['rows']),"best")), 
                functions.o(range['y']['has']))
    # if the['g'] == 'all' or the['g'] == 'copy':
    #     t1 = {'a':1, 'b':{'c':2, 'd':[3]}}
    #     t2 = functions.copy(t1)
    #     t2['b']['d'][0] = 10000
    #     print("b4",functions.o(t1),"\nafter",functions.o(t2))
    #     print("✅ pass: copy")


    # if the['g'] == 'all' or the['g'] == 'repcols':
    #     t = functions.repCols(functions.dofile(the['f']).get("cols"))
    #     for col in t.cols.all:
    #         print(vars(col))
    #     for row in t.rows:
    #         print(vars(row))
    #     print("✅ pass: repcols")


    # if the['g'] == 'all' or the['g'] == 'synonyms':
        
    #     t = functions.dofile(the['f'])["cols"]
    #     cols = functions.repCols(t)
    #     x = cols.cluster()
    #     functions.show(x)
    #     # functions.show(functions.repCols(functions.dofile(the['f']).get("cols")).cluster())
    #     print("✅ pass: synonyms")

        
    # if the['g'] == 'all' or the['g'] == 'reprows':
    #     t = functions.dofile(the['f'])
    #     rows = functions.repRows(t, functions.transpose(t['cols']))
    #     functions.map(rows.cols.all, functions.oo)
    #     functions.map(rows.rows, functions.oo)
    #     print("✅ pass: reprows")

    # if the['g'] == 'all' or the['g'] == 'prototypes':
    #     t = functions.dofile(the['f'])
        
    #     rows = functions.repRows(t, functions.transpose(t["cols"]))
    #     functions.show(rows.cluster())
    #     print("✅ pass: prototypes")

    # if the['g'] == 'all' or the['g'] == 'position':
    #     t = functions.dofile(the['f'])
    #     rows = functions.repRows(t, functions.transpose(t["cols"]))
    #     rows.cluster()
    #     functions.repPlace(rows)
    #     print("✅ pass: position")

    # if the['g'] == 'all' or the['g'] == 'repgrid':
    #     t = functions.dofile(the['f'])
    #     rows = functions.repRows(t, functions.transpose(t["cols"]))
    #     cols = functions.repCols(t["cols"])
    #     functions.show(rows.cluster())
    #     functions.show(cols.cluster())
    #     functions.repPlace(rows)
    #     print("✅ pass: repgrid")

    # print("======================================================================================================")
    # print('Test Cases')
    # print("======================================================================================================")

    # for f in ['./etc/data/repgrid_test1.json','./etc/data/repgrid_test2.json','./etc/data/repgrid_test3.json']:
    #     t = functions.dofile(f)
    #     rows = functions.repRows(t, functions.transpose(t["cols"]))
    #     cols = functions.repCols(t["cols"])
    #     functions.show(rows.cluster())
    #     functions.show(cols.cluster())
    #     functions.repPlace(rows)
    #     print("✅ pass: repgrid", f.split('/')[-1])

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