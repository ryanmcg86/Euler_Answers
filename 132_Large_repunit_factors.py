'''A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11 × 41 × 271 × 9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(109).
Link: https://projecteuler.net/problem=132'''

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
    
#Build a Solve function
def solve(limit, factors):
    #Define variables
    start = time.time()
    s = set()
    exp = 5
    
    #Solve the problem
    while len(s) < factors:
        if isPrime(exp) and pow(10, limit, exp) == 1:
            s.add(exp)
        exp += 2
        
    #Print the results
    print 'The sum of the first ' + str(factors) + ' factors '
    print 'of R(' + str(limit) + ') is ' + str(sum(s)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**9
factors = 40
solve(limit, factors)
