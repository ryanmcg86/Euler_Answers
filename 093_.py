'''A number chain is created by continuously adding the square of the 
digits in a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
Link: https://projecteuler.net/problem=92'''

#Imports
import time


#Build a solve function
def solve():
    #Define variables
    start = time.time()
    

    #Solve the problem	
    
    
    #Print the results
    
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
solve()
