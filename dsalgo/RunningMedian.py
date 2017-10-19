#!/bin/python3

import sys
from heapq import heappush as push
from heapq import heappushpop as pushpop

lowerHalf = []
upperHalf = []

def add(value):
    value = pushpop(upperHalf,value)
    value = -pushpop(lowerHalf,-value)
    if(len(upperHalf) <= len(lowerHalf)):
        push(upperHalf,value)
    else:
        push(lowerHalf,-value)

def getMedian():
    if(len(upperHalf) > len(lowerHalf)):
        return upperHalf[0]
    else:
        return (upperHalf[0] - lowerHalf[0])/2

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    add(a_t)
    print ('%.1f' %getMedian())
