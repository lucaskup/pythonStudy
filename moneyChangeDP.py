#!/bin/python3

import sys

dic = {}

def possibleChange(valor,coins,i):
    if valor == 0:
        return 1
    if valor < 0 or i >= len(coins):
        return 0
    if str(valor)+'-'+str(i) in dic:
        return dic[str(valor)+'-'+str(i)]
    r = possibleChange(valor - coins[i],coins,i) + possibleChange(valor,coins,i+1)
    dic[str(valor)+'-'+str(i)] = r
    return r

def make_change(coins, n):
    return possibleChange(n,coins,0)
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))

