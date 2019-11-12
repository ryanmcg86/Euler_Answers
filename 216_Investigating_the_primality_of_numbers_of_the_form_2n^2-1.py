'''Consider numbers t(n) of the form t(n) = 2n2-1 with n > 1.
The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
For n ≤ 10000 there are 2202 numbers t(n) that are prime.

How many numbers t(n) are prime for n ≤ 50,000,000 ?
Link: https://projecteuler.net/problem=216'''

#Imports
import time
from math import sqrt

#Build a modular square root function
def modular_sqrt(n, p):
    a = n % p
    if p % 4 == 3: return pow(a, (p + 1) >> 2, p)
    elif p % 8 == 5:
        v = pow(a << 1, (p - 5) >> 3, p)
        i = ((a * v * v << 1) % p) - 1
        return (a * v * i) % p
    elif p % 8 == 1:
        q, e = p - 1, 0
        while q & 1 == 0:
            e += 1
            q >>= 1
        n = 2
        while legs(n, p) != -1: n += 1
        w = pow(a, q, p)
        x = pow(a, (q + 1) >> 1, p)
        y = pow(n, q, p)
        r = e
        while True:
            if w == 1: return x
            v, k = w, 0
            while v != 1 and k + 1 < r:
                v = (v * v) % p
                k += 1
            if k == 0: return x
            d = pow(y, 1 << (r - k - 1), p)
            x, y = (x * d) % p, (d * d) % p
            w, r = (w * y) % p, k
    else: return a
    
#Build a Sieve of Eratosthenes funtion
def SoE(n): 
    prime, p = [False] * 2 + [True for i in range(n - 1)], 2
    while p**2 <= n: 
        if prime[p]: 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    return prime
    
#Build a legend symbol function
def legs(n, p):
    ls = pow(n, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    ps = SoE(int(sqrt(2 * lim**2 - 1)))
    sieve = [False, False] + [True] * (lim - 1)
    n = 2
    r = [p for p, b in enumerate(ps) if b and legs((p + 1) // 2, p) == 1]

    #Solve the problem
    for p in r:
        mr = modular_sqrt((p + 1) // 2, p)
        sieve[mr::p] = [False] * ((lim - mr) // p + 1)
        sieve[p - mr::p] = [False] * ((lim - (p - mr)) // p + 1)
        if n * n * 2 - 1 == p:
            sieve[n] = True
            n += 1
            while sieve[n] == False: n += 1
	
    ans = str(sum(sieve))
    lim = str(lim)

    #Print the results
    print('There are ' + ans + ' numbers t(n) for ')
    print('n <= ' + lim + ' that are prime.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 5 * 10**7
solve(lim)
