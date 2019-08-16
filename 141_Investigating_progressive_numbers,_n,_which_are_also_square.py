'''A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. 
In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 
are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102^2, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (10^12).
Link: https://projecteuler.net/problem=141'''

#Imports
import time
import math

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
    
#Build an isSquare function
def isSquare(n):
    return n**0.5 == int(n**0.5)
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = set()
    
    #Solve the problem
    for a in range(2, int(math.ceil(limit**(1/3.)))):
        for b in range(1, a):
            if b**2 * (a**3 + 1) >= limit:
                break
            if gcd(a, b) > 1:
                continue
            c = 1
            while True:
                n = a**3 * b * c**2 + c * b**2
                if n >= limit:
                    break
                if isSquare(n):
                    ans.add(n)
                c += 1
    
    ans = str(sum(ans))
    lim = str(limit)
    
    #Print the results
    print 'The sum of all progressive perfect squares '
    print 'below ' + lim + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**12
solve(limit)
