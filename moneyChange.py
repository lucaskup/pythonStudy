
#dictionary for memoization
dic = {}

def possibleChange(valor, coinsDisp):
    if valor == 0:
        return 1
    if valor < 0:
        return 0
    length = len(coinsDisp)
    if len(coinsDisp) == 0:
        return 0
    if str(coinsDisp[0])+'-'+ str(valor) in dic:
        return dic[str(coinsDisp[0])+'-'+ str(valor)]
    soma = 0
    

    listaCapada = coinsDisp[1:length]
    for i in range(valor//coinsDisp[0]+1):
        if i != 0 or length > 1:
            soma += possibleChange(valor - coinsDisp[0]*i,listaCapada)     
    dic[str(coinsDisp[0])+'-'+ str(valor)] = soma    
    return  soma

n, m = [int(c_temp) for c_temp in input().strip().split(' ')]

coins = [int(c_temp) for c_temp in input().strip().split(' ')]

print(possibleChange(n,coins))
#print(dic)
