'''It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third 
differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area 
and whose perimeters do not exceed one billion (1,000,000,000).
Link: https://projecteuler.net/problem=94'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    x1    = 2
    y1    = 1
    x2    = 4
    y2    = 2
    ans   = 0
    
    #Solve the problem
    #Pells function allows us to solve this quickly.
    while x2 < limit:
        if (x2 - 1) % 3 == 0:
            a = (x2 - 1) // 3
            if (a - 1) * (3 * a**2 - 1 + 2 * a)**0.5 % 4 == 0 and a > 1:
                ans += x2
        elif (x2 + 1) % 3 == 0:
            a = (x2 + 1) // 3
            if (a + 1) * (3 * a**2 - 1 - 2 * a)**0.5 % 4 == 0:
                ans += x2
        x2temp = x2
        y2temp = y2
        x2     = x2temp * x1 + y1 * y2temp * 3
        y2     = y2temp * x1 + y1 * x2temp
    
    #Print the results
    print 'The sum of the perimeters of all almost equilateral triangles with integral '
    print 'side lengths and area and whose perimeters do not exceed ' + str(limit) + ' is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
solve()
