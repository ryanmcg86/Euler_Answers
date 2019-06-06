'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
Link: https://projecteuler.net/problem=10'''

#Imports
import time

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

#Build a findSum function
def findSum(num):
    start = time.time()
    sop = 0
    for i in range(2, 2000000):
        if isPrime(i):
            sop += i
    
    print 'The sum of all primes below ' + str(num) + ' is ' + str(sop) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Find the sum of all primes below 2000000
num = 2000000
findSum(num)
