'''Consider the fraction, n/d, where n and d are positive integers. 
If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
Link: https://projecteuler.net/problem=73'''

#Imports
import time

#Build a solve function
def solve(limit, left, right):
    #Define variables
    start  = time.time()
    count  = 0
    top    = 0
    stack  = []
    oleft  = str(left)
    oright = str(right)
    
    #Solve the problem
    for i in range(0, limit / 2 + 1):
        stack.append(i)
        
    while True:
        med = left + right
        if med > limit:
            if top > 0:
                left  = right
                top  -= 1
                right = stack[top]
            else:
                break
        else:
            count     += 1
            stack[top] = right
            top       += 1
            right      = med

    #Print the results
    print 'For d <= ' + str(limit) + ', ' + str(count) + ' fractions lie '
    print 'between 1 / ' + oleft + ' and 1 / ' + oright + ' in the sorted '
    print 'set of reduced proper fractions.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 12000
solve(limit)
