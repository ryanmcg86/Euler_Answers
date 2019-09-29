'''A composite is a number containing at least two prime factors. 
For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 
4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
Link: https://projecteuler.net/problem=187'''

#Imports
import time

#Build a Sieve Of Eratosthenes function
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    ans = []
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            ans.append(p)
    return ans
    
#Build a binary search function
def bin_search(n, lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == n: return mid
        elif lst[mid] > n: right = mid - 1
        else: left = mid + 1
    if n > lst[mid]: return mid
    else: return mid - 1

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    primes = SieveOfEratosthenes(lim // 2)
    ans = 0

    #Solve the problem
    for n in range(bin_search(int(lim**0.5), primes) + 1):
        ans += bin_search(int(lim / primes[n]), primes) - n + 1
        
    ans = str(ans)
    lim = str(lim)

    #Print the results
    print('There are ' + ans + ' composite integers, n < ' + lim + ', which')
    print('have precisely two, not necessarily distinct, prime factors.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**8
solve(lim)
