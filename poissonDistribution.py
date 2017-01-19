
def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

def p(k,l):
    return (l**k*2.71828**(-l))/factorial(k)

print(round(p(3,2),3))
