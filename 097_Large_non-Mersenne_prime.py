'''The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form 2^6972593 − 1; it contains exactly 2,098,960 digits. 
Subsequently other Mersenne primes, of the form 2^p − 1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457 + 1.

Find the last ten digits of this prime number.
Link: https://projecteuler.net/problem=97'''

#Imports
import time

#Build a solve function
def solve(base, exp):
    #Define variables
    start = time.time()
    n = 2
    
    #Solve the problem
    for x in range(2, exp + 1):
        n *= 2
        if n > (10**10 - 1):
            n -= 10**10
            
    ans = str(int(str(base * n)[-10:]) + 1)
    
    #Print the results
    print 'The last ten digits of the prime number, '
    print str(base) + '^' + str(exp) + ' + 1, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
base = 28433
exp = 7830457
solve(base, exp)
