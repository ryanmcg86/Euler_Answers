'''Euler discovered the remarkable quadratic formula:

n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. 
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and 
certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n = 0.
Link: https://projecteuler.net/problem=27'''

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

#Build a function that returns the product
#of the coefficients, a and b, for the quadratic
#expression that produces the maximum number
#of primes for consecutive values of n, starting with
#n = 0.
def ProdOfCoefficients(posRange):
    start = time.time()
    
    maxN = 0
    maxA = 0
    maxB = 0
    
    #When n = 0, n^2 + a * n + b simplifies to simply, b.
    #Since the result needs to be prime, the b's range isn't
    #-(posRange) to posRange, instead, it is the primes from
    #2 to posRange.
    possibleBs = [2, 3]
    for i in range(5, posRange, 6):
        if isPrime(i):
            possibleBs.append(i)
        if isPrime(i + 2):
            possibleBs.append(i + 2)
            
    for a in range(-posRange + 1, posRange):
        for b in possibleBs:
            #When n = 1, the function simplifies to 1 + a + b
            #So this check saves us some work below
            if not isPrime(1 + a + b):
                continue
            n = 0
            function = n**2 + a * n + b
            while isPrime(function):
                n += 1
                function = n**2 + a * n + b
            if n > maxN:
                maxN = n
                maxA = a
                maxB = b
                
    print 'The product of the coefficients, a and b, for '
    print 'the quadratic expression that produces the maximum '
    print 'number of primes for consecutive values of n, '
    print 'starting with n = 0, is ' + str(maxA * maxB) + '.\n'
    sign = '+ '
    if maxA < 0:
        sign = '- '
        maxA = -1 * maxA
    print 'The quadratic expression was n^2 ' + sign + str(maxA) + '*n + ' + str(maxB) + ', '
    if sign == '- ':
        maxA = -1 * maxA
    print 'where a = ' + str(maxA) + ' and b = ' + str(maxB) + ', and it produces '
    print str(maxN) + ' consecutive primes starting with n = 0.\n'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
posRange = 1000
ProdOfCoefficients(posRange)
