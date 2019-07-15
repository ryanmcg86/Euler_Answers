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
    #Define variables
    start  = time.time()
    
    #Solve the problem
    

    #Print the results
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 100
solve(limit)
