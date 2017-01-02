mport sys

def median(lista):
    #print(lista)
    median = 0
    #lista = sorted(lista)
    length = len(lista)
    if length%2 == 0:
        median = (lista[length//2] + lista[(length//2)-1])/2
    else:
        median = lista[length//2]
    return median

n = int(input())
x = [int(c_temp) for c_temp in input().strip().split(' ')]
x = sorted(x)

q2 = int(median(x))
q1 = 0
q3 = 0
length = len(x)
if(length%2==0):
    q1 = median(x[0:length//2])
    q3 = median(x[length//2:length])
else:
    q1 = median(x[0:length//2])
    q3 = median(x[length//2+1:length])
q1 = int(q1)
q3 = int(q3)
print(q1)
print(q2)
print(q3)
