'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
Link: https://projecteuler.net/problem=35'''

#Imports
import time

#Build a build-a-prime-sieve function
def build_sieve(n):
    if n < 2:
        return []
    if n < 3:
        return [2]
    if n < 5:
        return [2, 3]
    if n < 7:
        return [2, 3, 5]
    prime_sieve = [2, 3, 5, 7]
    if n < 11:
        return prime_sieve
    for i in range(11, n, 6):
        for j in range(i, i + 3, 2):
            flag = True
            for k in prime_sieve:
                if k > int(j**0.5) + 1:
                    break
                if j % k == 0:
                    flag = False
            if flag == True:
                prime_sieve.append(j)
    return prime_sieve
    
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
    
#Build an isCircular function
def isCircular(n):
    orig = str(n)
    num = orig[1:] + orig[:1]
    prime = isPrime(int(num))
    if not prime:
        return False
    while prime and num != orig:
        num = num[1:] + num[:1]
        prime = isPrime(int(num))
        if not prime:
            return False
    return True

#Build a Solve function
def Solve(num):
    start = time.time()
    
    sieve = build_sieve(num)
    count = 0
    for prime in sieve:
        if isCircular(prime):
            count += 1
        
    count = str(count)
    
    print 'There are ' + count + ' circular primes below ' + str(num) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 1000000
Solve(num)