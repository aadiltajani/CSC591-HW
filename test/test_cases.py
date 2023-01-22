import sys
sys.path.append("./src")
import functions
import NUM
import Sym
the = {'h': False, 'd': False, 's': 937162211, 'g': 'all'}

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
    sym = Sym.SYM()
    for i in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(i)
    val = 'a' == sym.mid() and 1.379 == functions.rnd(sym.div())
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


test_the()
test_rand()
test_sym()
test_num()