'''A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; 
for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, 
for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
Link: https://projecteuler.net/problem=129'''

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
    
#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
    
#Build an A(n) function
def A(n):
    if isPrime(n) or gcd(n, 10) != 1:
        return None
    x, k = 1, 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    L = limit + 1
    n = L
    
    #Solve the problem
    while A(n) < L:
        n += 2
        
    #Print the results
    print 'The least value of n for which A(n) '
    print 'first exceeds ' + str(limit) + ' is ' + str(n) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**6
solve(limit)
