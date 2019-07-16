'''It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits 
for all the irrational square roots.
Link: https://projecteuler.net/problem=80'''

#Imports
import time
from decimal import *

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    getcontext().prec = 102
    total = 0
    
    #Solve the problem
    for i in range(1, limit + 1):
        num = str(Decimal(i).sqrt())
        if '.' in num:
            num = num.replace('.', '')[:100]
            for j in num:
                total += int(j)
    
    #Print the results
    print 'The total of the digital sums of the first ' + str(limit) + ' decimal '
    print 'digits for all the irrational square roots is ' + str(total) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 100
solve(limit)
