#!/bin/python3

import sys
def lessSignificants(num):
    i = 0
    while 2**i <= num:
	    i += 1
    return (2**(i-1)-1) - num + 2**(i-1)

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    limite = lessSignificants(x)
    print(limite)
