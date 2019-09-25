'''For any integer n, consider the three functions

f1,n(x,y,z) = xn+1 + yn+1 − zn+1
f2,n(x,y,z) = (xy + yz + zx)*(xn-1 + yn-1 − zn-1)
f3,n(x,y,z) = xyz*(xn-2 + yn-2 − zn-2)

and their combination

fn(x,y,z) = f1,n(x,y,z) + f2,n(x,y,z) − f3,n(x,y,z)

We call (x,y,z) a golden triple of order k if x, y, and z are all rational numbers of the form a / b with
0 < a < b ≤ k and there is (at least) one integer n, so that fn(x,y,z) = 0.

Let s(x,y,z) = x + y + z.
Let t = u / v be the sum of all distinct s(x,y,z) for all golden triples (x,y,z) of order 35.
All the s(x,y,z) and t must be in reduced form.

Find u + v.
Link: https://projecteuler.net/problem=178'''

#Imports
import time
from fractions import Fraction as F

#Build a g function
def g(x, y):
    z = x + y
    a, b = int(z.numerator**0.5), int(z.denominator**0.5)
    if a**2 == z.numerator and b**2 == z.denominator:
        return F(a, b)
    else:
        return F(-1)

#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    s, n = set(), set()

    #Solve the problem
    for a in range(1, limit):
        for b in range(a + 1, limit + 1):
            n.add(F(a, b))
            
    for x in n:
        for y in n:
            z = x + y
            if z in n: s.add(x + y + z)
            z = g(x**2, y**2)
            if z in n: s.add(x + y + z)
            z = (x**-1 + y**-1)**-1
            if z in n: s.add(x + y + z)
            z = g(x**-2, y**-2)**-1
            if z in n: s.add(x + y + z)
                
    t = sum(s)
    ans = str(t.denominator + t.numerator)
    l = str(limit)
        
    #Print the results
    print 'When t = u / v is the sum of all distinct '
    print 's(x, y, z) for all golden triples (x, y, z) '
    print 'of order ' + l + ', u + v = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 35
solve(limit)
