'''Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers 
below one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?
Link: https://projecteuler.net/problem=113'''

#Imports
import time

#Build a solve function
def solve(exp):
    #Declare variables
    start = time.time()
    count = 0
    
    #Solve the problem
    for i in range(1, exp + 1):
        for j in range(8, 10):
            count += nCr(j + i, i)
        count -= 10
    
    ans = str(count)
    
    #Print the results
    print 'There are ' + ans + ' numbers below 10^' + str(exp) + ' that not bouncy.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
exp = 100
solve(exp)
