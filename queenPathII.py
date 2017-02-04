#!/bin/python3

import sys

def calcHoriLeft(posX):
    return posX - 1
def calcHoriRight(posX,size):
    return size - posX
def calcVertUp(posY,size):
    return size - posY
def calcVerDown(posY):
    return posY - 1
def calcDiagonal1Up(posX,posY,size):
    return min([size-posX,size-posY])
def calcDiagonal1Down(posX,posY):
    return min([posX-1,posY-1])
def calcDiagonal2Up(posX,posY,size):
    return min([size-posY,posX-1])
def calcDiagonal2Down(posX,posY,size):
    return min([size-posX,posY-1])
def yDiagonalPrincipal(posX,posY,x):
    num = posY - posX
    return x + num
def yDiagonalSecundaria(posX,posY,x):
    num = posX + posY
    return num - x

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

vertD = calcVerDown(rQueen)
vertU = calcVertUp(rQueen,n)
horiL = calcHoriLeft(cQueen)
horiR = calcHoriRight(cQueen,n)
diag1U = calcDiagonal1Up(cQueen,rQueen,n)
diag1D = calcDiagonal1Down(cQueen,rQueen)
diag2U = calcDiagonal2Up(cQueen,rQueen,n)
diag2D = calcDiagonal2Down(cQueen,rQueen,n)
#print(vertB,vertC,horiE,horiD,d1c,d1b,d2c,d2b)

total = vertD + vertU + horiL + horiR + diag1U + diag1D + diag2U + diag2D

closestVertD = None
closestVertU = None
closestHoriL = None
closestHoriR = None

closestDiag1U = None
closestDiag1D = None
closestDiag2U = None
closestDiag2D = None


for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    #se atrapalha na vertical
    if cQueen == cObstacle:
        #se atrapalha em cima
        if rQueen < rObstacle:
            if closestVertU is None or closestVertU[1] > rObstacle:
                closestVertU = [cObstacle,rObstacle]
        #se atrapalha em baixo
        else:
            if closestVertD is None or closestVertD[1] < rObstacle:
                closestVertD = [cObstacle,rObstacle]
    #se atrapalha na Horizontal
    elif rQueen == rObstacle:
        #se atrapalha a esquerda
        if cQueen > cObstacle:
            if closestHoriL is None or closestHoriL[0] < cObstacle:
                closestHoriL = [cObstacle,rObstacle]
        #se atrapalha a direita
        else:
            if closestHoriR is None or closestHoriR[0] > cObstacle:
                closestHoriR = [cObstacle,rObstacle]
    #se atrapalha a diagonal principal
    elif rObstacle == yDiagonalPrincipal(cQueen,rQueen,cObstacle):
        #se atrapalha acima

        if rObstacle > rQueen:
            if closestDiag1U is None or closestDiag1U[1] > rObstacle:
                closestDiag1U = [cObstacle,rObstacle]
        else:
            if closestDiag1D is None or closestDiag1D[1] < rObstacle:
                closestDiag1D = [cObstacle,rObstacle]
    #se atrapalha a diagonal secundaria
    elif rObstacle == yDiagonalSecundaria(cQueen,rQueen,cObstacle):
        #se atrapalha acima

        if rObstacle > rQueen:
            if closestDiag2U is None or closestDiag2U[1] > rObstacle:
                closestDiag2U = [cObstacle,rObstacle]
        else:
            if closestDiag2D is None or closestDiag2D[1] < rObstacle:
                closestDiag2D = [cObstacle,rObstacle]

if closestVertU is not None:
    total -= 1+calcVertUp(closestVertU[1],n)
    #print(total,'verup')
if closestVertD is not None:
    total -= 1+calcVerDown(closestVertD[1])
    #print(total,'verdow')
if closestHoriL is not None:
    total -= 1+calcHoriLeft(closestHoriL[0])
    #print(total,'horl')
if closestHoriR is not None:
    total -= 1+calcHoriRight(closestHoriR[0],n)
    #print(total,'horir')
if closestDiag1U is not None:
    total -= 1+calcDiagonal1Up(closestDiag1U[0],closestDiag1U[1],n)
    #print(total,'d1u')
if closestDiag1D is not None:
    total -= 1+calcDiagonal1Down(closestDiag1D[0],closestDiag1D[1])
    #print(total,'diud',closestDiag1D)
if closestDiag2U is not None:
    total -= 1+calcDiagonal2Up(closestDiag2U[0],closestDiag2U[1],n)
    #print(total,'d2u')
if closestDiag2D is not None:
    total -= 1+calcDiagonal2Down(closestDiag2D[0],closestDiag2D[1],n)
    #print(total,'d2d')
print(total)
