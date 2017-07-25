#!/bin/python3

import sys

def distanceFromPoint(x1,y1,x2,y2):
    return (((x2-x1)**2)+((y2-y1)**2))**0.5

def isInsideCircle(x,y):
    return True if distanceFromPoint(x,y,circleX,circleY)<=r else False

def getOtherCordinates(x1,y1,x3,y3):
    cx = (x1+x3)/2
    cy = (y1+y3)/2

    vx = x1 - cx
    vy = y1 - cy # // vector c->(x1,y1)
    ux = vy
    uy = -vx#          // rotate through 90 degrees
    x2 = cx + ux
    y2 = cy + uy # // one of the endpoints of other diagonal
    x4 = cx - ux
    y4 = cy - uy# // the other endpoint
    return [[x2,y2],[x4,y4]]

def isInsideSquare(x1,y1,x3,y3,x,y):
    temp = getOtherCordinates(x1,y1,x3,y3)
    x2 = temp[0][0]
    y2 = temp[0][1]
    x4 = temp[1][0]
    y4 = temp[1][1]

    a1 = areaPolygon3(x,y,x1,y1,x2,y2)
    a2 = areaPolygon3(x,y,x2,y2,x3,y3)
    a3 = areaPolygon3(x,y,x3,y3,x4,y4)
    a4 = areaPolygon3(x,y,x1,y1,x4,y4)
    aT = areaPolygon(x1,y1,x2,y2,x3,y3,x4,y4)
    if a1 + a2 + a3 + a4 > aT:
        return False

    return True

def areaPolygon(x1,y1,x2,y2,x3,y3,x4,y4):
    return abs(((x1*y2 - y1*x2) + (x2*y3-y2*x3) +(x3*y4-y3*x4) +(x4*y1-y4*x1))/2)
def areaPolygon3(x1,y1,x2,y2,x3,y3):
    return abs(((x1*y2 - y1*x2) + (x2*y3-y2*x3) +(x3*y1-y3*x1))/2)
w = 20
h = 16

circleX = 9
circleY = 6
r = 5

x1 = 16
y1 = 14
x3 = 8
y3 = 14
# your code goes here

for y in range(h):
    for x in range(w):
        if isInsideCircle(x,y) or isInsideSquare(x1,y1,x3,y3,x,y):
            print('#',end='')
        else:
            print('.',end='')
    print('')
