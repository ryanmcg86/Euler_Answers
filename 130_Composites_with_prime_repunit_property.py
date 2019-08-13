'''A number consisting entirely of ones is called a repunit. 
We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, 
for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5, 
and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).
Link: https://projecteuler.net/problem=130'''

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
def solve(limit):
    #Define variables
    start = time.time()
    dnp = set()
    n = 91
    
    #Solve the problem
    while len(dnp) < limit:
        if not isPrime(n) and pow(10, n - 1, 9 * n) == 1:
            dnp.add(n)
        n += 2
        
    ans = str(sum(dnp))
    limit = str(limit)
        
    #Print the results
    print 'The sum of the first ' + limit + ' composite values '
    print 'of n for which GCD(n, 10) == 1 and '
    print 'n - 1 is divisible by A(n) is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 25
solve(limit)
