# Python program to output all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)]
    ans = []
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1): 
        if prime[p]: 
            ans.append(p)
    return ans
