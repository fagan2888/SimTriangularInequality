# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:16:59 2015

@author: stephenhky
"""

import numpy as np
from operator import add

def isTriangular(y1, y2):
    x1 = min(y1, y2)
    x2 = max(y1, y2)
    return (x1<0.5) and (x2>0.5) and (x2-x1<0.5)
    
def sim1(numtimes=10000):
    y1 = np.random.uniform(low=0.0, high=1.0, size=numtimes)
    y2i = np.random.uniform(low=0.0, high=1.0, size=numtimes)
    y2 = y1 + y2i*(1.-y1)
    return zip(y1, y2)
    
def sim2(numtimes=10000):
    y1 = np.random.uniform(low=0.0, high=1.0, size=numtimes)
    y2 = np.random.uniform(low=0.0, high=1.0, size=numtimes)
    return zip(y1, y2)
    
if __name__ == '__main__':
    numtimes = 1000000
    num1 = reduce(add, map(lambda s: 1 if isTriangular(*s) else 0, 
                           sim1(numtimes=numtimes)))
    num2 = reduce(add, map(lambda s: 1 if isTriangular(*s) else 0, 
                       sim2(numtimes=numtimes)))
    print "prob1 = ", num1 / float(numtimes)
    print "prob2 = ", num2 / float(numtimes)    
