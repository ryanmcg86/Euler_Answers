'''A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
Link: https://projecteuler.net/problem=56'''

#Imports
import time

#Build a solve function
def solve(n):
    #Define variables
    start = time.time()
    maxSum = 0

    #Solve the problem
    for a in range(1, 100):
        for b in range(1, 100):
            num = sum(int(digit) for digit in str(a**b))
            if num > maxSum:
                maxSum = num

    #Print the results
    print 'When a and b are less than ' + str(n) + 'the maximum digital sum is ' + str(maxSum) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 100
solve(n)
