'''The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
Link: https://projecteuler.net/problem=6'''

#Imports
import time

#Sum of squares function
def sumOfsquares(n):
    return sum(i**2 for i in range(1, n + 1))
    
#Square of sum function
def squareOfsum(n):
    return ((n * (n + 1)) / 2)**2

#Difference function
def diff(n):
    start = time.time()
    diff = str(squareOfsum(n) - sumOfsquares(n))
    
    print 'The difference between the sum of the squares of the first ' + str(n) 
    print 'natural numbers and the square of the sum is ' + diff + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 100
diff(n)
