'''Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), 
green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row
measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
Link: https://projecteuler.net/problem=117'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Declare variables
    l = [1, 2, 3, 4]
    f = [0] * (limit + 1)
    f[1] = 1
    
    #Solve the problem
    for n in range(2, limit + 1):
        f[n] = sum([f[n - m] + (1 if n == m else 0)) for m in l if n - m >= 0])
        
    ans = str(f[limit])
    
    #Print the results
    print 'A row measuring ' + str(limit) + ' rows can be tiled '
    print ans + ' different ways.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 50
solve(limit)
