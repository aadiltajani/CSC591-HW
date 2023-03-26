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
    print("\t\ttruee", stats.bootstrap( {8, 7, 6, 2, 5, 8, 7, 3}, 
                                {8, 7, 6, 2, 5, 8, 7, 3}),
                functions.cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3}, 
                            {8, 7, 6, 2, 5, 8, 7, 3}))
    print("\t\tfalse", stats.bootstrap(  {8, 7, 6, 2, 5, 8, 7, 3},  
                                    {9, 9, 7, 8, 10, 9, 6}),
                functions.cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3},  
                            {9, 9, 7, 8, 10, 9, 6})) 
    print("\t\tfalse", 
                stats.bootstrap({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                                {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}),
                functions.cliffsDelta({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                                {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}))

def egpre():
    print("\neg3")
    d = 1
    for i in range(10):
      t1 = []
      t2 = []
      for j in range(32):
          t1.append(stats.gaussian(10,1))
          t2.append(stats.gaussian(d * 10,1))
      val = True if d<1.1 else False
      print("\t",d,val,stats.bootstrap(t1,t2),stats.bootstrap(t1,t1))
      d = round(d + 0.05, 2)

def egfive():
    print('\n\nfive\n')
    for rx in stats.tiles(stats.scottKnot(
         [functions.RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),
         functions.RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"),
         functions.RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"),
         functions.RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"),
         functions.RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")])):
        print(rx['name'],rx['rank'],rx['show'])     

def egsix():
    print('\n\nsix\n')
    for rx in stats.tiles(stats.scottKnot(
      [functions.RX({101,100,99,101,99.5,101,100,99,101,99.5},"rx1"),
      functions.RX({101,100,99,101,100,101,100,99,101,100},"rx2"),
      functions.RX({101,100,99.5,101,99,101,100,99.5,101,99},"rx3"),
      functions.RX({101,100,99,101,100,101,100,99,101,100},"rx4")])):
      print(rx['name'],rx['rank'],rx['show'])
    

def egtiles():
    print('\n\ntiles\n')
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for _ in range(1000):
        a.append(stats.gaussian(10,1))
    for _ in range(1000):
        b.append(stats.gaussian(10.1,1))
    for _ in range(1000):
        c.append(stats.gaussian(20,1))
    for _ in range(1000):
        d.append(stats.gaussian(30,1))
    for _ in range(1000):
        e.append(stats.gaussian(30.1,1))
    for _ in range(1000):
        f.append(stats.gaussian(10,1))
    for _ in range(1000):
        g.append(stats.gaussian(10,1))
    for _ in range(1000):
        h.append(stats.gaussian(40,1))
    for _ in range(1000):
        j.append(stats.gaussian(40,3))
    for _ in range(1000):
        k.append(stats.gaussian(10,1))
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(stats.RX(v,"rx" + str (k+1) ))
    rxs = stats.rxs_sort(rxs)
    for rx in stats.tiles(rxs):
        print("",rx['name'],rx['show'])

def egsk():
    print('\n\nsk\n')
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for _ in range(1000):
        a.append(stats.gaussian(10,1))
    for _ in range(1000):
        b.append(stats.gaussian(10.1,1))
    for _ in range(1000):
        c.append(stats.gaussian(20,1))
    for _ in range(1000):
        d.append(stats.gaussian(30,1))
    for _ in range(1000):
        e.append(stats.gaussian(30.1,1))
    for _ in range(1000):
        f.append(stats.gaussian(10,1))
    for _ in range(1000):
        g.append(stats.gaussian(10,1))
    for _ in range(1000):
        h.append(stats.gaussian(40,1))
    for _ in range(1000):
        j.append(stats.gaussian(40,3))
    for _ in range(1000):
        k.append(stats.gaussian(10,1))
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(functions.RX(v,"rx" + str(k + 1)))
    for rx in stats.tiles(stats.scottKnot(rxs)):
        print("",rx['rank'],rx['name'],rx['show'])

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