'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
Link: https://projecteuler.net/problem=7'''

#Imports
import time

#Build a suffix function
def buildSuffix(num):
    suffs = ['th', 'st', 'nd', 'rd']
    suff = suffs[0]
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        lastdigit = int(str(num)[-1])
        if lastdigit < len(suffs):
            suff = suffs[lastdigit]
    return suff

#Build an isPrime function
def isPrime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Build an nthPrime function
def nthPrime(n):
    if n < 1: return 'Error'
    if n == 1: return 2
    if n == 2: return 3
    count, i, p = 2, 5, 5
    while count < n:
        if isPrime(i):
            count += 1
            p = i
        if count == n: break
        if isPrime(i + 2):
            count += 1
            p = i + 2
        i += 6
    return p

#nthPrime function
def solve(n):
    #Define variables
    start = time.time()
    
    #Solve the problem
    ans = str(nthPrime(n))
    
    suff = buildSuffix(n)
    n = str(n)
    
    #Print the results
    print('The ' + n + suff + ' prime number is ' + str(ans) + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Find the 10001st prime
n = 10001
solve(n)
