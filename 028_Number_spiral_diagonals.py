'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals (21, 7, 1, 3, 13, 17, 5, 9, and 25) is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
Link: https://projecteuler.net/problem=28'''

#Imports
import time

#Build a spiralSum function
def spiralSum(n):
    if n % 2 != 0: s, a, b, c = (n - 1) // 2, 30, 26, 3
    else:          s, a, b, c =  n      // 2,  6,  8, 0
    return (16 * s**3 + a * s**2 + b * s + c) // 3


#Build a answer function
def answer(num):
    start = time.time()
    
    ans = str(spiralSum(num))
    grid = str(num) + ' by ' + str(num)
    
    print 'The sum of the numbers on the diagonals in a ' + grid + ' spiral is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
num = 1001
answer(num)
