'''If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
and two discs were taken at random, it can be seen that the probability of taking two blue discs, 
P(BB) = (15 / 21) × (14 / 20) = 1 / 2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.
Link: https://projecteuler.net/problem=100'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    b = 15
    n = 21
    
    #Solve the problem (using Diophantine Numbers)
    while n < limit:
        bnext = 3 * b + 2 * n - 2
        nnext = 4 * b + 3 * n - 3
        b = bnext
        n = nnext
    
    #Print the results
    print 'In the first arrangement to contain more than ' + str(limit) + ' discs in total, '
    print 'the number of blue discs that the box would contain is ' + str(b) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**12
solve(limit)
