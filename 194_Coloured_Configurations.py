'''Consider graphs built with the units 
A: *---*
   |\*/|
   | | |
   | * |
   | | |
   |/*\|
   *---*

and B: 
   *---*
   |\*/|
   | | |
   | * |
   | | |
   |/*\|
   *   *

, where the units are glued along the vertical edges as in the graph
   *---*---*---*---*
   |\*/|\*/|\*/|\*/|
   | | | | | | | | |
   | * | * | * | * |
   | | | | | | | | |
   |/*\|/*\|/*\|/*\|
   *---*   *   *---* .

A configuration of type (a,b,c) is a graph thus built of a units A and b units B, 
where the graph's vertices are coloured using up to c colours, so that no two adjacent vertices have the same colour.
The compound graph above is an example of a configuration of type (2,2,6), in fact of type (2,2,c) for all c ≥ 4.

Let N(a, b, c) be the number of configurations of type (a, b, c).
For example, N(1, 0, 3) = 24, N(0, 2, 4) = 92928 and N(2, 2, 3) = 20736.

Find the last 8 digits of N(25, 75, 1984).
Link: https://projecteuler.net/problem=194'''

#Imports
import time

#Build a factorial function
def fact(n):
    return fact(n - 1) * n if n > 1 else 1
    
#Build the N function
def N(a, b, c):
    one = c * (c - 1)
    two = (c - 2) * (c**4 - 7 * c**3 + 20 * c**2 - 29 * c + 19)
    three = (c**2 - 2 * c + 3) * (c - 2)**3
    four = fact(a + b) / (fact(a) * fact(b))
	return one * (two)**a * (three)**b * four

#Build a Solve function
def solve(a, b, c, digits):
    #Define variables
    start = time.time()

    #Solve the problem
    ans = str(N(a, b, c))
    ans = ans[len(ans) - digits:]
    a, b, c, digits = str(a), str(b), str(c), str(digits)

    #Print the results
    print 'The last ' + digits + ' digits of '
    print 'N(' + a + ', ' + b + ', ' + c + ') are ' + ans + '.'
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
a, b, c, digits = 25, 75, 1984, 8
solve(a, b, c, digits)
