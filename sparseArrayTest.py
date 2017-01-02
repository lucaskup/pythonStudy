mport sys

dic = {}
n = int(input())
for i in range(n):
    word = input()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
q = int(input())
for i in range(q):
    word = input()
    print(dic.get(word,0))
