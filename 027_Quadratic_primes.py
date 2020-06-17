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
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Build a Sieve of Eratosthenes function 
def SoE(n): 
    prime = [False] * 2 + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n: 
        if prime[p]: 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    return [i for i in range(n) if prime[i]]

#Build a function that returns the product
#of the coefficients, a and b, for the quadratic
#expression that produces the maximum number
#of primes for consecutive values of n, starting with
#n = 0.
def PoC(posRange):
    #Declare Variabeles
    start = time.time()
    maxN, maxA, maxB, sign = 0, 0, 0, '+ '
    
    #When n = 0, n^2 + a * n + b simplifies to simply, b.
    #Since the result needs to be prime, the b's range isn't
    #-(posRange) to posRange, instead, it is the primes from
    #2 to posRange.
    possibleBs = SoE(posRange)
    
    #Solve the problem
    for a in range(-posRange + 1, posRange):
        for b in possibleBs:
            #When n = 1, the function simplifies to 1 + a + b
            #So this check saves us some work below
            if not isPrime(1 + a + b):
                continue
            n = 2
            function = n**2 + a * n + b
            while isPrime(function):
                n += 1
                function = n**2 + a * n + b
            if n > maxN:
                maxN, maxA, maxB = n, a, b
                
    maxN, maxA, maxB, ans = str(maxN), str(maxA), str(maxB), str(maxA * maxB)
	exp = 'n^2 + ' + maxA + '*n + ' + maxB
                
    print('The product of the coefficients, a and b, for ')
	print('the quadratic expression that produces the maximum ')
	print('number of primes for consecutive values of n, ')
	print('starting with n = 0, is ' + ans + '.\n')
	print('The quadratic expression was ' + exp + ', ')
	print('where a = ' + maxA + ' and b = ' + maxB + ', and it produces ')
	print(maxN + ' consecutive primes starting with n = 0.\n')
	print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
posRange = 1000
PoC(posRange)
