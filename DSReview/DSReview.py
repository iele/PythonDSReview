#!/usr/bin/env python

import time
import algorithm.BinarySearchTree

starttime = time.time()
l = algorithm.BinarySearchTree.BinarySearchTree(range(1,100))
l.postorder(l.top)
endtime = time.time()

print endtime - starttime
