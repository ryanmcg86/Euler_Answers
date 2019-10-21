'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
Link: https://projecteuler.net/problem=10'''

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

#Build a findSum function
def findSum(num):
    #Define variables
    start = time.time()
    
    #Solve the problem
    ans = str(sum(SoE(n)))
    n = str(n)
    
    print('The sum of all primes below ' + n + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Find the sum of all primes below 2000000
num = 2000000
findSum(num)
