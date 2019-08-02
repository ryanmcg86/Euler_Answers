'''A row measuring seven units in length has red blocks with a minimum length of three units placed on it, 
such that any two red blocks (which are allowed to be different lengths) are separated by at least one grey square. 
There are exactly seventeen ways of doing this.

p114.png
How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. 
For example, on a row measuring eight units in length you could use red (3), grey (1), and red (4).
Link: https://projecteuler.net/problem=114'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Declare variables
    start = time.time()
    f = [1, 1, 1, 3]
    
    #Solve the problem
    for n in range(3, limit + 1):
        fn = f[3] - f[2] - f[1] + 1
        f = [fn, f[0], f[1], f[3] + fn]
        
    ans = str(f[0])
    
    #Print the results
    print 'A row measuring ' + str(limit) + ' units in length '
    print 'can be filled in ' + ans + ' different ways.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 50
solve(limit)
