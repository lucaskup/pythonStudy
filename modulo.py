# function to normalize modulo 10^9+7 for coding competitions
def norm(x): 
    mod = 1e9+7 
    return x if x<mod else int(x-mod) 

print(norm(1000000007))
