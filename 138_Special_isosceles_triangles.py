'''Consider the isosceles triangle with base length, b = 16, and legs, L = 17.

By using the Pythagorean theorem it can be seen that the height of the triangle,
h = √(17^2 − 8^2) = 15, which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length, 
and this is the second smallest isosceles triangle with the property that h = b ± 1.

Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.
Link: https://projecteuler.net/problem=138'''

#Imports
import time
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    x, y, lSum = 0, 1, 0
    
    #Solve the problem
    for i in range(1, limit + 2):
        tx = x
        ty = y
        x = (-9 * tx) + (4 * ty) - 4
        y = (20 * tx) - (9 * ty) + 8
        if abs(y) != 1:
            lSum += abs(y)
            
    lSum = str(lSum)
    limit = str(limit)
    
    #Print the results
    print 'The sum of L for the ' + limit + ' smallest isosceles '
    print 'triangles for which h = b + 1 or b - 1 and both '
    print 'b and L are positive integers is ' + lSum + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 12
solve(limit)

'''This can be solved by solving the Diophantine quadratic equation where we replace b/2 with x and L with y:

2x +- 1 = sqrt(y^2 - x^2)

(2x +- 1)^2 = y^2 - x^2

4x^2 +- 4x + 1 = y^2 - x^2

5x^2 +- 4x - y^2 + 1 = 0

5x^2 - y^2 +- 4x + 1 = 0

The recursive values for this Diophantine quadratic equation, with base cases x(0) = 0 and y(0) = 1, are:

x(n + 1) = (-9 * x(n)) + (4 * y(n)) - 4

and 

y(n + 1) = (20 * x(n)) - (9 * y(n)) + 8

Since y is a substitution for L, to sum up the 12 smallest L values, we just loop through these equations 12 times,
skipping L = 1, because if L = 1, then b and h can't both be an integer.
'''
