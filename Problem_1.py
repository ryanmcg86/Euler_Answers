'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link: https://projecteuler.net/problem=1'''

#Imports
import time

#Run function
def SumOfMults(n):
    start = time.time()
    multiples = set()
    for i in range(0, n, 3):
        multiples.add(i)
    for i in range(0, n, 5):
        multiples.add(i)
    print 'The sum of all the multiples of 3 or 5 below ' + str(n) + ' is ' + str(sum(multiples)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 1000
SumOfMults(n)
