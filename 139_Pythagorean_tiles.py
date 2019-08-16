'''Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. 
It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in 
the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used 
to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean 
triangles would allow such a tiling to take place?
Link: https://projecteuler.net/problem=139'''

#Imports
import time
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    x, y, c = 1, 1, 0
    p, q, r, s = 3, 4, 2, 3
    
    #Solve the problem
    while x + y < limit:
        xn = x
        yn = y
        x  = (p * xn) + (q * yn)
        y  = (r * xn) + (s * yn)
        c += (limit - 1) / (x + y)
            
    c = str(c)
    lim = str(limit)
    
    #Print the results
    print 'Given that the perimeter of the right angle '
    print 'is less than ' + lim + ', ' + c + ' pythagorean '
    print 'triangles would allow such a tiling to take place.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**8
solve(limit)

'''This can be solved by solving the Diophantine quadratic equation 

The recursive values for this Diophantine quadratic equation, with base cases x(0) = 1 and y(0) = 1, are:
x(n + 1) = (3 * x(n)) + (4 * y(n))
and 
y(n + 1) = (2 * x(n)) + (3 * y(n))
'''
