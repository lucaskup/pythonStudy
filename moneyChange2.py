def possibleChange(valor,coins,i):
    if valor == 0:
        return 1
    if valor < 0 or i >= len(coins):
        return 0
    return possibleChange(valor - coins[i],coins,i) + possibleChange(valor,coins,i+1)
print(possibleChange(10,[1,5],0))
