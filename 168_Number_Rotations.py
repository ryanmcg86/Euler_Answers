'''Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.
It can be verified that 714285=5×142857.
This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10100, that have this property.
Link: https://projecteuler.net/problem=168'''

#Imports
import time
   
#Build a Solve function
def solve(digits):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for m in range(1, 9 + 1):
        for d in range(1, 9 + 1):
            n = d
            t = 1
            for k in range(1, 100):
                n = 10 * (n * m % (10 * t)) + d
                t *= 10
                if n >= t and n * m == d * t + n / 10:
                    ans = (ans + n) % 10**digits
    
    ans = str(ans)

    #Print the results
    print 'The last 5 digits of the sum of all integers n, '
    print '10 < n < 10^100, that have the given property are ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
digits = 5
solve(digits)
