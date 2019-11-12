'''Consider the right angled triangle with sides a=7, b=24 and c=25. The area of this triangle is 84, 
which is divisible by the perfect numbers 6 and 28.
Moreover it is a primitive right angled triangle as gcd(a,b)=1 and gcd(b,c) = 1.
Also c is a perfect square.

We will call a right angled triangle perfect if
-it is a primitive right angled triangle
-its hypotenuse is a perfect square

We will call a right angled triangle super-perfect if
-it is a perfect right angled triangle and
-its area is a multiple of the perfect numbers 6 and 28.

How many perfect right-angled triangles with c ≤ 10^16 exist that are not super-perfect?
Link: https://projecteuler.net/problem=218'''

#Imports
import time

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    l = str(lim)
    lim, ans = int((2 * lim)**0.5), 0
    
    #Solve the problem
    for m in range(1, lim):
        for n in range(1, m):
            if m % 2 == n % 2: continue
            if gcd(m, n) != 1: continue
            c = m**2 + n**2
            if c > lim: break
            if c**0.5 - int(c**0.5) != 0: continue
            if ((m**2 - n**2) * 2 * m * n) // 2) % 84 != 0:
                ans += 1
                continue
                
    ans, lim = str(ans), l
    
    #Print the results
    print('There are ' + ans + ' perfect right-angled triangles with ')
    print('c <= ' + lim + ' that are not super-perfect.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Build a mathematically proven optimized Solve function
def fast_solve(lim):
    #Define variables
    start, lim = time.time(), str(lim)
    
    #Solve the problem/Print the results
    print('There are 0 perfect right-angled triangles with ')
    print('c <= ' + lim + ' that are not super-perfect.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**16
solve(lim)
fast_solve(lim)
