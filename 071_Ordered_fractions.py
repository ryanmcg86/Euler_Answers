'''Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d) = 1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.
Link: https://projecteuler.net/problem=71'''

#Imports
import time
import math

#Build a function that, given a denominator and
#a fraction, returns the largest possible numerator
#where the resultant fraction is below the given fraction
def bigFrac(denom, value):
    return math.floor((denom * value[0] - 1) / float(value[1]))

#Build a solve function
def solve(limit, value):
    #Define variables
    start = time.time()
    bestNum   = 0
    bestDenom = 1
    minDenom  = 1
    q         = limit
    a         = value[0]
    b         = value[1]
    
    #Solve the problem
    while q >= minDenom:
        p = bigFrac(q, value)
        if bestNum * q < p * bestDenom:
            bestNum   = p
            bestDenom = q
            delta     = a * q - b * p
            minDenom  = q / (delta + 1)
        q -= 1

    fracStr = str(value[0]) + ' / ' + str(value[1])
    ans = str(int(bestNum))
    
    #Print the results
    print 'For the set of reduced proper fractions for d <= ' + str(limit)
    print 'in ascending order of size, the numerator of the '
    print 'fraction immediately to the left of ' + fracStr + ' is ' + ans + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 10**6
value = [3, 7]
solve(limit, value)
