'''The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. 
Given that n is a positive integer, the equation, x^2 − y^2 − z^2 = n, has exactly one solution when n = 20:

13^2 − 10^2 − 7^2 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
Link: https://projecteuler.net/problem=136'''

#Imports
import time
    
#Build a Solve function
def solve(limit, sol):
    #Define variables
    start = time.time()
    solutions = [0] * (limit + 1)
    ans = 0
    
    #Solve the problem
    for u in range(1, limit + 1):
        for v in range(1, (limit / u) + 1):
            if ((u + v) % 4) == 0:
                if (3 * v) > u:
                    if ((3 * v - u) % 4) == 0:
                        solutions[u * v] += 1
                
    for i in solutions:
        if i == sol:
            ans += 1
            
    ans = str(ans)
    limit = str(limit)
    sol = str(sol)
        
    #Print the results
    print 'There are ' + ans + ' values of n less than ' + limit
    print 'with exactly ' + sol + ' distinct solution(s).'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 5 * 10**7
sol = 1
solve(limit, sol)
