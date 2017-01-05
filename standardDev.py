#!/bin/python3

import sys
def mean(x):
    m = 0
    
    for num in x:
        m += num
    m = m / len(x)
    return m
def standardDev(x):
    m = mean(x)
    stdDev = 0
    for num in x:
        stdDev += (num - m)**2
    stdDev = (stdDev/n)**(1/2)
    return stdDev

n = int(input())
x = [int(c_temp) for c_temp in input().strip().split(' ')]

print("%.1f" % standardDev(x))
