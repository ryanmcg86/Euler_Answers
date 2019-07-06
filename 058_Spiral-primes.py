'''Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of 
primes along both diagonals first falls below 10%?
Link: https://projecteuler.net/problem=58'''

#Imports
import time

#Build an isPrime function
def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
 
#Build a spiral function
def spiral(n):
    spiral = []
    #1 instead of 0, as n**2 will never be prime, this speeds it up a bit.
    for i in range(1, 4):
        spiral.append(n**2 - i * (n - 1))
    return spiral
  
#Build a primeCount function   
def primeCount(n):
    count = 0
    for i in spiral(n):
        if isPrime(i):
            count += 1
    return count

#Build a solve function
def solve(val):
    #Define variables
    start  = time.time()
    n      = 3
    frac   = 1.0
    primes = 0

    #Solve the problem
    while frac >= val:
        primes += primeCount(n)
        frac = primes / float(2 * n - 1)
        if frac >= val:
            n += 2

    #Print the results
    print 'The side length of the square spiral for which the ratio of primes '
    print 'along both diagonals first falls below ' + str(val) + ' is ' + str(n) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
val = 0.10
solve(n)
