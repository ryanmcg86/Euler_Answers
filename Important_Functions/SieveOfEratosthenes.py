# Python program to output all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

def SoE(n): 
    prime = [False] * 2 + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n: 
        if prime[p]: 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    return [i for i in range(n) if prime[i]]
