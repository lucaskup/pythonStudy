
def factorial(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return factorial(n) / (factorial(x) * factorial(n-x))

#Calculates Binomial Distribution of a given number
#where:
# p is the probability of success
# n is the number of experiments
# x is the number of successes
def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)
