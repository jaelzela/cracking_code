#!/bin/python

import sys

def insertElement(a, e):
    if len(a) == 0:
        a.append(e)
    i = 0
    while i < len(a):
        if e < a[i]:
            a.insert(i, e)
            break
        i += 1

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    #insertElement(a, a_t)
    a.append(a_t)
    a.sort()
    if len(a) % 2 == 0:
        median = round(float(a[(len(a)/2)-1] + a[len(a)/2])/2, 1)
    else:
        median = round(float(a[len(a)/2]), 1)
    print median