'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Link: https://projecteuler.net/problem=5'''

#Imports
import time

#Lowest Common Multiple function
def lcm(a, b):
    a1, b1 = a, b
    while b:
        a, b = b, a % b
    return a1 * b1 // a

#Run function
def run(n):
    start = time.time()
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
            
    print 'The smallest positive number that is evenly divisible by all of '
    print 'the numbers from 1 to ' + str(n) + '  is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 20
run(n)
