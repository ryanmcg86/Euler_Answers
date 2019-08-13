'''Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, 
the least value of the positive integer, n, for which the equation, x^2 − y^2 − z^2 = n, 
has exactly two solutions is n = 27:

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
Link: https://projecteuler.net/problem=135'''

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
limit = 10**6
sol = 10
solve(limit)
