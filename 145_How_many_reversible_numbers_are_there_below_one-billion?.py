'''Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
Link: https://projecteuler.net/problem=145'''

#Imports
import time
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    count = 0
    
    #Solve the problem
    for i in range(2, limit + 1):
        if i % 2 == 0: 
            count += 20 * 30**(i / 2 - 1)
        elif i % 4 == 3: 
            count += 100 * 500**(i / 4)
            
    ans = str(count)
    lim = str(limit)

    #Print the results
    print 'There are ' + ans + ' reversible numbers below 10^' + lim + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 9
solve(limit)
