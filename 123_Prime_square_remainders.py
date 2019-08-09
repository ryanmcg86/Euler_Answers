'''Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn^2.

For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.
Link: https://projecteuler.net/problem=123'''

#Imports
import time

#Build an isPrime function
def isPrime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i  = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#Build a nums function
def nums():
    i = 2
    while True:
        yield i
        i += 1
        
#Build a remainder function
def r(n, a):
    if n % 2 == 0:
        return 2
    elif 2 * n * a < a**2:
        return 2 * n * a
    else:
        return 2 * n * a - a**2

#Build a solve function
def solve(limit):
    #Declare variables
    start = time.time()
    n = 1
    primes = (i for i in nums() if isPrime(i))
    found = False
    
    #Solve the problem
    while not found:
        a = next(primes)
        if r(n, a) > limit:
            found = True
        else:
            n += 1
            
    ans = str(n)
        
    #Print the results
    print 'The least value of n for which the remainder '
    print 'first exceeds ' + str(limit) + ' is ' + ans + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**10
solve(limit)
