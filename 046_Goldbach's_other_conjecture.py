'''It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9  = 7  + 2×1^2
15 = 7  + 2×2^2
21 = 3  + 2×3^2
25 = 7  + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
Link: https://projecteuler.net/problem=46'''

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
    
#Build an updateSieve function
def updateSieve(n):
    i = prime_sieve[-1]
    while i < n:
        i += 2
        if isPrime(i):
            prime_sieve.append(i)
            
#Build an isTwiceSquare function
def isTwiceSquare(n):
    updateSieve(n)
    if n in prime_sieve:
        return True
    for i in prime_sieve:
        for j in range(1, int(n**0.5) + 1):
            if n == i + (2 * j**2):
                return True
    return False

#Build a solve function
def solve():
    #Define variables
    start       = time.time()
    prime_sieve = [2, 3, 5, 7]
    ans         = 9
    
    while isTwiceSquare(ans):
        ans += 2
    
    #Print the results
    print 'The smallest odd composite that cannot be written as'
    print 'the sum of a prime and twice a square is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
