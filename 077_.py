'''It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
Link: https://projecteuler.net/problem=76'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    digits = [x for x in range(1, limit + 1)]
    ways = [1] + [0] * limit
    
    #Solve the problem
    for i in digits:
        for j in range(i, limit + 1):
            ways[j] += ways[j - i]
    
    ans = str(ways[-1] - 1)
    
    #Print the results
    print 'There are ' + ans + ' different ways to sum up to ' + str(limit) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 100
solve(limit)
