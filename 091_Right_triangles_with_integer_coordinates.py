'''The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate 
lies between 0 and 2 inclusive; that is,

0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
Link: https://projecteuler.net/problem=91'''

#Imports
import time

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    result = limit**2 * 3

    #Solve the problem	
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            fact = gcd(x, y)
            a = (y * fact) / x
            b = ((limit - x) * fact) / y
            result += min(a, b) * 2
            
    ans = str(result)

    #Print the results
    print 'Given that 0 <= x1, y1, x2, y2 <= ' + str(limit) + ','
    print ans + ' right triangles can be formed.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 50
solve(limit)
