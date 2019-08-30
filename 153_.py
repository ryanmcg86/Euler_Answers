'''As we all know the equation x2=-1 has no solutions for real x. 
If we however introduce the imaginary number i this equation has two solutions: x = i and x = -i. 
If we go a step further the equation (x-3)^2 = -4 has two complex solutions: x = 3+2i and x = 3-2i. 
x = 3+2i and x = 3-2i are called each others' complex conjugate. 
Numbers of the form a + bi are called complex numbers. 
In general a + bi and a − bi are each other's complex conjugate.

A Gaussian Integer is a complex number a + bi such that both a and b are integers. 
The regular integers are also Gaussian integers (with b = 0). 
To distinguish them from Gaussian integers with b ≠ 0 we call such integers "rational integers." 
A Gaussian integer is called a divisor of a rational integer n if the result is also a Gaussian integer. 
If for example we divide 5 by 1 + 2i we can simplify 5 / (1 + 2i) in the following manner:

Multiply numerator and denominator by the complex conjugate of 1 + 2i: 1 − 2i. 
The result is 5 / (1 + 2i) = 5 / (1 + 2i) * (1 − 2i) / (1 − 2i) = 5 * (1 − 2i) / (1 − (2i)^2) = 5 * (1 − 2i) / (1 − (−4)) 
= 5 * (1 − 2i) / 5 = 1 − 2i.

So 1 + 2i is a divisor of 5. 
Note that 1 + i is not a divisor of 5 because 5 / (1 + i) = 5 / 2 − 5 / 2i.

Note also that if the Gaussian Integer (a + bi) is a divisor of a rational integer n, 
then its complex conjugate (a − bi) is also a divisor of n.

In fact, 5 has six divisors such that the real part is positive: {1, 1 + 2i, 1 − 2i, 2 + i, 2 − i, 5}. 
The following is a table of all of the divisors for the first five positive rational integers:

n    Gaussian integer divisors                 Sum s(n) of 
     with positive real part                   these divisors

1    1                                          1
2    1, 1 + i, 1 - i, 2                         5
3    1, 3                                       4
4    1, 1 + i, 1 - i, 2, 2 + 2i, 2 - 2i, 4	   13
5    1, 1 + 2i, 1 - 2i, 2 + i, 2 - i, 5        12

For divisors with positive real parts, then, we have: ∑s(n) for n = 1 to 5 = 35.

For ∑s(n) for n = 1 to 10^5 = 17924657155.

What is ∑s(n) for n = 1 to 10^8?
Link: https://projecteuler.net/problem=153'''

#Imports
import time
    
#Build a greatest common denominator function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
    
#Build a ss function
def ss(x):
    s = 0
    i = 1
    while i <= x:
        j = x / i
        ii = x / j
        s += (ii + i) * (ii - i + 1) * j / 2
        i = ii + 1
    return s
   
#Build a Solve function
def solve(nmax):
    #Define variables
    start = time.time()
    s = ss(nmax)
    
    #Solve the problem
    for a in range(1, int(nmax**0.5) + 1):
        for b in range(1, min(a, int((nmax - a * a)**0.5)) + 1):
            if gcd(a, b) == 1:
                num = 0
                if a == b: num = a
                else: num = a + b
                s += ss(nmax / (a * a + b * b)) * 2 * num
    
    #Print the results
    print 'The sum of all of the Gaussian integer divisors '
    print 'with a positive real part for all positive '
    print 'integers from 1 to ' + str(nmax) + ' is ' + str(s) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
nmax = 10**8
solve(nmax)
