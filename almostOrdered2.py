#!/usr/bin/python


def evalSwap():
    global listOutOfOrder
    listOutOfOrder = []
    for i in range(len(listaIni)):
        if listaIni[i] != listaOrd[i]:
            listOutOfOrder.append(i)
        if len(listOutOfOrder) > 2:
            return False
    if len(listOutOfOrder) != 2:
        return False
    return listaIni[listOutOfOrder[0]] == listaOrd[listOutOfOrder[1]] and listaIni[listOutOfOrder[1]] == listaOrd[listOutOfOrder[0]]

def evalReverse():
    global listOutOfOrder
    listOutOfOrder = []
    for i in range(len(listaIni)):
        if listaIni[i] != listaOrd[i]:
            listOutOfOrder.append(i)
    length = len(listOutOfOrder)
    print(listOutOfOrder)
    if length > 1:
        for i in range(length):
            if i > 0 and (listOutOfOrder[i] - listOutOfOrder[i-1] != 1 and not(listOutOfOrder[i] - listOutOfOrder[i-1] == 2 and i == length//2 )):
                print('Droga',listOutOfOrder[i],listOutOfOrder[i-1])
                return False
            
            if listaIni[listOutOfOrder[i]] != listaOrd[listOutOfOrder[length -1 - i]]:
                return False
    return True

def alreadySorted():
    for i in range(len(listaIni)):
        if listaIni[i] != listaOrd[i]:
            return False
    return True
f = open('testCases.txt', 'r')
#numberElements = f.readline()
#listaIni = [int(c_temp) for c_temp in f.readline().strip().split(' ')]
listaIni =[0,5,4,3,2,1,6]
listaOrd = sorted(listaIni)
listOutOfOrder = []

if alreadySorted():
    print('yes')
elif evalSwap():
    print('yes')
    print('swap',listOutOfOrder[0]+1,listOutOfOrder[1]+1)
elif evalReverse():
    print('yes')
    print('reverse',listOutOfOrder[0]+1,listOutOfOrder[len(listOutOfOrder)-1]+1)
    #print(listaIni)
else:
    print('no')   
print(listOutOfOrder[0],listOutOfOrder[len(listOutOfOrder)-1])
