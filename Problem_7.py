'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
Link: https://projecteuler.net/problem=7'''

#Imports
import time

#Build a suffix function
def buildSuffix(num):
    suff = 'th'
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        if   int(str(num)[-1]) == 1:
            suff = 'st'
        elif int(str(num)[-1]) == 2:
            suff = 'nd'
        elif int(str(num)[-1]) == 3:
            suff = 'rd'
    return suff

#Build an isPrime function
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#nthPrime function
def nthPrime(n):
    start = time.time()
    count = 0
    i = 2
    while count < 10001:
        if isPrime(i):
            count += 1
        if count < 10001:
            i += 1
    
    suff = buildSuffix(n)
    
    print 'The ' + str(n) + suff + ' prime number is ' + str(i) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Find the 10001st prime
n = 100001
nthPrime(n)
