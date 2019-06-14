'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
Link: https://projecteuler.net/problem=41'''

#Imports
from itertools import permutations as p
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

#Build a Solve function
def Solve():
    #Define variables
    start  = time.time()
    digits = []
    pans   = []
    primes = []
    
    #Create the pandigitals to test
    #Note: 9 and 8-digit pandigitals can't be prime 
    #b/c the sum of 1 through 9 and 1 through 8
    # is 45 and 36 (both divisible by 3), respectively.
    for i in range(1, 8):
        digits.append(i)
        perm = p(digits)
        for j in list(perm):
            j = list(j)
            num = ''
            for k in range(0, len(j)):
                num += str(j[k])
            pans.append(int(num))
    
    #Find the prime pandigitals
    for i in range(0, len(pans)):
        if isPrime(pans[i]):
            primes.append(pans[i])
    
    #Find the largest prime pandigital
    ans = str(max(primes))

    #Print the results
    print 'The largest pandigital prime is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
Solve()
