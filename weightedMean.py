n = int(input())
x = [int(c_temp) for c_temp in input().strip().split(' ')]
w = [int(c_temp) for c_temp in input().strip().split(' ')]


sumWeights = 0
weightedMean = 0

for i in range(n):
    weightedMean += x[i]*w[i]
    sumWeights += w[i]
print(round(weightedMean/sumWeights,1))
