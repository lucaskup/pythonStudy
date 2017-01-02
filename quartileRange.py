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
def quartileRange(x):
    q1 = 0
    q3 = 0
    length = len(x)
    if(length%2==0):
        q1 = median(x[0:length//2])
        q3 = median(x[length//2:length])
    else:
        q1 = median(x[0:length//2])
        q3 = median(x[length//2+1:length])
    q1 = q1
    q3 = q3
    return q3 - q1

n = int(input())
x = [int(c_temp) for c_temp in input().strip().split(' ')]
weight = [int(c_temp) for c_temp in input().strip().split(' ')]
lista = []
for i in range(n):
    for j in range(weight[i]):
        lista.append(x[i])
lista = sorted(lista)
print("%.1f" % round(quartileRange(lista),1))
