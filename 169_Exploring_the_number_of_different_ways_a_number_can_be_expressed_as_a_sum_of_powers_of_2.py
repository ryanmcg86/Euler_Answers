'''Define f(0) = 1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 
using each power no more than twice.

For example, f(10) = 5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10^25)?
Link: https://projecteuler.net/problem=169'''

#Imports
import time
   
#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    p = [0, 1]              #p[1 - i] = number of ways to add i to next bit
    lim = str(n)
    
    #Solve the problem
    while n:
        p[n % 2] = sum(p)   # set p for least significant bit
        n /= 2
        
    ans = str(p[1])

    #Print the results
    print 'When f(n) is the number of different ways n can be expressed '
    print 'as a sum of integer powers of 2 using each power no more than '
    print 'twice, f(' + lim + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 10**25
solve(n)
