'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
Link: https://projecteuler.net/problem=15'''

#Imports
import time

#Build a factorial function
def factorial(num):
    ans = 1
    for i in range(num, 1, -1):
        ans *= i
    return ans
    
#Build an nCr function
def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

#Solution function
def Solution(a, b):
    start = time.time()
    n = a + b
    r = a
    print 'When only being able to move to the right and down, '
    print 'there are ' + str(nCr(n, r)) + ' total routes through a ' + str(a) + 'x' + str(b) + ' grid.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
a = 20
b = 20
Solution(a, b)
