def dv_sum(cpfSemDv):
    dv1 = 0
    dv2 = 0
    sum = 0
    temp = 0
    for i in range(len(cpfSemDv)):
        temp = int(cpfSemDv[8-i])
        dv1 += temp*(9 - ((i)%10))
        dv2 += temp*(9 - ((i+1)%10))
        sum += temp
    dv1 = (dv1%11)%10
    dv2 += dv1*9
    dv2 = (dv2%11)%10
    #print(dv1,dv2)
    return sum+dv1+dv2
#print(dv(input()))
def sum_d(n):
    r = 0
    for i in n:
        r += int(i)
    return r

#print(sum_d(input()))
hashTable = {}
for j in range(100):
    hashTable[j] = 0
for i in range(999999999):
    cpfSemDv = ('000000000' + str(i))[-9:]
    soma = dv_sum(cpfSemDv)
    hashTable[soma] += 1
    print('Calculating: ',i,str(int(i/999999999*100))+'%\r',end='')
print(hashTable)
