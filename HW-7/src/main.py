import random
import sys
import functions
import sys
import stats
import numpy as np

sys.path.append("./HW-7/src")

the={'bootstrap':512, 'conf':0.05, 'cliff':0.4, 'cohen':0.35, 'Fmt':"%6.2f", 'width':40}

def egok():
    print('\nok')
    random.seed(1)

def egsample():
    print('\n\nsample')
    for i in range(10):
        print('\t'+''.join(stats.samples(["a","b","c","d","e"])))

def egnum():
    print('\n\nnum\n')
    n = functions.num([1,2,3,4,5,6,7,8,9,10])
    print("", n['n'], n['mu'], n['sd'], sep='\t')

def eggauss():
    print('\n\ngauss\n')
    t = []
    for i in range(10**4):
        t.append(stats.gaussian(10, 2))
    n = functions.num(t)
    print("", n['n'], n['mu'], n['sd'], sep='\t')


def egbootmu():
    print('\n\nbootmu\n')
    a = []
    for i in range(100):
        a.append(stats.gaussian(10, 1))
    print("","mu","sd","cliffs","boot","both", sep='\t')
    print("","--","--","------","----","----", sep='\t')
    for mu in np.arange(10, 11.1, 0.1):
        mu = round(mu, 1)
        b = []
        for i in range(100):
            b.append(stats.gaussian(mu, 1))
        cl = functions.cliffsDelta(a, b)
        bs = stats.bootstrap(a, b)
        print("", mu, 1, cl, bs, cl and bs, sep='\t')

def egbasic():
    print('\n\nbasic\n')

def egpre():
    print('\n\npre\n')

def egfive():
    print('\n\nfive\n')

def egsix():
    print('\n\nsix\n')

def egtiles():
    print('\n\ntiles\n')

def egsk():
    print('\n\nsk\n')

egok()
egsample()
egnum()
eggauss()
egbootmu()
egbasic()
egpre()
egfive()
egsix()
egtiles()
egsk()