'''Build a triangle from all positive integers in the following way:

 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8) = 60 and S(9) = 37.

You are given that S(10000) = 950007619.

Find  S(5678027) + S(7208785).
Link: https://projecteuler.net/problem=196'''

#Imports
import time
from math import sqrt, floor

#Build a Sieve of Eratosthenes
def SoE(n): 
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
    
#Build the S function
def S(lines):
    lim = max(lines)
    primes = SoE(floor(sqrt((lim + 2) * (lim + 3) // 2)) + 1)
    tot = 0
    for n in lines:
        start = (n - 3) * (n - 2) // 2 + 1
        stop  = (n + 2) * (n + 3) // 2 + 1 - start
        sieve = [True for i in range(stop)]
        for p in primes:
            x = start % p
            if x:
                x = p - x
            for i in range(x, stop, p):
                sieve[i] = False
        a = (-n, -2)
        b = (-n, 2 - n)
        c = (-n, 2 - n * 2)
        d = (1 - n, 2 - n * 2)
        e = (1 - n, 4 - n * 2)
        f = (2 - n, 4 - n * 2)
        g = (2 - n, 2)
        h = (n - 1, n + 1)
        i = (n - 1, -2)
        j = (n - 1, n * 2)
        k = (n, n * 2)
        l = (n, n * 2 + 2)
        m = (n + 1, n * 2 + 2)
        o = (n + 1, 2)
        q = (-n, n)
        r = (1 - n, n - 1)
        s = (1 - n, n + 1)
        t = (2 - n, n)
        mask = (a, b, c, d, e, f, g, h, i, j, k, l, m, o, q, r, s, t)
        begin = (n - 1) * n // 2 + 1 - start
        end = (n + 1) * n // 2 - start - 1
        for i in range(begin, end):
            if sieve[i]:
                for u, v in mask:
                    if sieve[i + u] and sieve[i + v]:
                        tot += i + start
                        break
    return tot

#Build a Solve function
def solve(a, b):
    #Define variables
    start = time.time()
  
    #Solve the problem
    ans = str(S((a, b)))
    a, b = str(a), str(b)

    #Print the results
    print('S(' + a + ') + S(' + b + ') = ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
a = 5678027
b = 7208785
solve(a, b)
