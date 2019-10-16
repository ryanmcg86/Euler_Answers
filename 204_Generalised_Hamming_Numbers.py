'''A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?
Link: https://projecteuler.net/problem=204'''

#Imports
import time
    
#Build a Sieve of Eratosthenes function
def SoE(n):
    prime = [False] * 2 + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(n + 1):
        if prime[p]: ans.append(p)
    return ans
    
#Build a count function
def count(primeIndex, product, ps, lim):
    if primeIndex == len(ps):
        if product <= lim: return 1
        else: return 0
    else:
        result = 0
        while product <= lim:
            result += count(primeIndex + 1, product, ps, lim)
            product *= ps[primeIndex]
        return result

#Build a Solve function
def solve(lim, ham):
    #Define variables
    start = time.time()
    ps = SoE(ham)
    index, product = 0, 1
    
    #Solve the problem
    ans = str(count(index, product, ps, lim))
    lim, ham = str(lim), str(ham)

    #Print the results
    print('There are ' + ans + ' generalised Hamming numbers ')
    print('of type ' + ham + ' which don''t exceed ' + lim + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**9
ham = 100
solve(lim, ham)
