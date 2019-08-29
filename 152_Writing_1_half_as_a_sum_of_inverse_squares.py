'''There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

12=122+132+142+152+172+1122+1152+1202+1282+1352
In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, the remaining two being: 
{2, 3, 4, 6, 7, 9, 10, 20, 28, 35, 36, 45} and {2, 3, 4, 6, 7, 9, 12, 15, 28, 30, 35, 36, 45}.

How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers between 2 and 80 inclusive?
Link: https://projecteuler.net/problem=151'''

#Imports
import time
from fractions import Fraction as f
import functools

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
    
#Build a greatest common denominator function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
    
#Build an lowest common multiple function
def lcm(a, b):
    return a * b / gcd(a, b)
    
#Build a maxprime function
def maxprime(ii, primes):
    for p in reversed(primes):
        for i in reversed(ii):
            if i % p == 0:
                return i
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    s = [f(0)]
    ii = list(range(2, limit + 1))
    primes = [i for i in range(limit) if isPrime(i)]
    
    #Solve the problem
    while ii:
        i = maxprime(ii, primes)
        ii.remove(i)
        l = functools.reduce(lcm, ii, 2)
        s = [x for x in s + [x + f(1, i**2) for x in s] if l**2 % x.denominator == 0]
	
    ans = sum(1 for x in s if x == f(1, 2))
    
    #Print the results
    print 'There are ' + str(ans) + ' ways to write the '
    print 'number 1/2 as a sum of inverse squares using '
    print 'distinct integers between 2 and ' + str(limit) + ' inclusive.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 80
solve(limit)
