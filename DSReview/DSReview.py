#!/usr/bin/env python

import random
import time
import algorithm.DoubleLink

rand = random.Random()
s = []
for i in range(0, 4):
    s.append(rand.randint(0, 1000))

starttime = time.time()
l = algorithm.DoubleLink.DoubleLink(range(0,9))
l.invert()
l.printl()
endtime = time.time()
print endtime - starttime
