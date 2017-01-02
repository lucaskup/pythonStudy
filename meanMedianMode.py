#!/bin/python3

import sys

n = int(input())
x = [int(c_temp) for c_temp in input().strip().split(' ')]

mean = 0
median = 0
mode = 0
dic = {}

x = sorted(x)
for num in x:
    mean += num
    if num in dic:
        dic[num] += 1    
    else:
        dic[num] = 1
mean = mean/n
if n%2 == 0:
    median = (x[n//2] + x[(n//2)-1])/2
else:
    median = x[n//2]

lista =  sorted(dic.items(), key=lambda e: (-e[1], e[0]))
mode = lista[0][0]
    
print(mean)
print(median)
print(mode)
