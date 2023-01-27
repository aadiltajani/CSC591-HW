import sys
import getopt
import functions
import NUM
import SYM
n = len(sys.argv)
cli_list = sys.argv[1:]
shorts = 'dg:hs:f:'
longs = ['dump', 'go=', 'help', 'seed=', 'file=']
the = {'h': False, 'd': False, 's': 937162211, 'g': 'all', 'f': '../etc/data/auto93.csv'}
help = """script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = ../etc/data/auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
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

if the['h']:
    print(help)
else:
    if the['g'] == 'all' or the['g'] == 'the':
        if not functions.oo(the):
            print("❌ fail: eg")
        else:
            print("✅ pass: eg")
    if the['g'] == 'all' or the['g'] == 'rand':
        if not rand():
            print("❌ fail: rand")
        else:
            print("✅ pass: rand")
    if the['g'] == 'all' or the['g'] == 'sym':
        Sym = SYM.sym()
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
        val = 11/7 == num.mid() and 0.787 == functions.rnd(num.div())
        if not val:
            print("❌ fail: num")
        else:
            print("✅ pass: num")
