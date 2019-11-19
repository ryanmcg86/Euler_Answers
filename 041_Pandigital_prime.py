'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
Link: https://projecteuler.net/problem=41'''

#Imports
from itertools import permutations as p
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
def Solve(n = 10**7):
    #Define variables
    start  = time.time()
    pans, primes, ans = [], [], 0
    
    #Create the pandigitals to test
    #Note: pandigitals can only be prime if they
    #have a length of 4 or 7. Anything other length
    #is either greater than 10, or results in a number
    #divisible by 3, and therefore not prime.
    for i in [4, 7]:
        for pan in list(p([j for j in range(1, i + 1)])):
            pans.append(int(''.join(str(digit) for digit in list(pan))))
    
    #Find the prime pandigitals
    for i in range(len(pans)):
        if isPrime(pans[i]): primes.append(pans[i])
    
    #Find the largest prime pandigital under n
    if n <= primes[0]:
	    print('There are no pandigital primes < ' + str(n) + '.')
    else:
        for i in range(len(primes)):
            if primes[i] >= n:
                ans = str(primes[i - 1])
                break
        if ans == 0:
            ans, n = str(primes[-1]), str(n)
            print('The largest pandigital prime is ' + ans + '.')
        else: 
            n = str(n)
            print('The largest pandigital prime < ' + n + ' is ' + ans + '.')

    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
Solve()
