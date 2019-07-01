'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
Link: https://projecteuler.net/problem=49'''

#Imports
import time
from itertools import permutations as p

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

#Build a solve function
def solve():
    #Declare variables
    start = time.time()
    ans = ''
    
    for i in range(1000, 10000):
        primes = []
        
        for number in p(str(i)):
            num = int(''.join(digit for digit in number))
            if isPrime(num):
                primes.append(num)
                
        primes = list(set(primes))
        relevantPrimes = []
        
        for a in range(0, len(primes) - 1):
            for b in range(a + 1, len(primes)):
                if abs(primes[a] - primes[b]) == 3330:
                    relevantPrimes.append(primes[a])
                    relevantPrimes.append(primes[b])
                    
        relevantPrimes = sorted(list(set(relevantPrimes)))
        ans = ''.join(str(j) for j in relevantPrimes)
        
        if len(ans) == 12 and ans != '148748178147':
            break

    #Print the results
    print 'The 12-digit number formed by concatenating '
    print 'the three terms in this sequence is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
