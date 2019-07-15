'''It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
Link: https://projecteuler.net/problem=76'''

#Imports
import time

#Build a solve function
def solve(limit):
    start = time.time()
    digits = [x for x in range(1, limit + 1)]
    
    final = digits[-1]
    ways = [1] + [0] * final
    for i in digits:
        for j in range(i, final + 1):
            ways[j] += ways[j - i]
    
    ans = str(ways[-1] - 1)
    
    print 'There are ' + ans + ' different ways to sum up to ' + str(limit) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 100
solve(limit)
