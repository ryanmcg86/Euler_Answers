'''Let x be a real number.
A best approximation to x for the denominator bound d is a rational number (r / s) in reduced form, with s ≤ d, 
such that any rational number which is closer to x than (r / s) has a denominator larger than d:

|(p / q) − x| < |(r / s) − x| ⇒ q > d
For example, the best approximation to √13 for the denominator bound 20 is (18 / 5) and the best approximation to 
√13 for the denominator bound 30 is (101 / 28).

Find the sum of all denominators of the best approximations to √n for the denominator bound 10^12, 
where n is not a perfect square and 1 < n ≤ 100000.
Link: https://projecteuler.net/problem=192'''

#Imports
import time
import fractions as frac
import decimal as d

#Build a Solve function
def solve(lim, bound):
    #Define variables
    start = time.time()
    d.getcontext().prec = 55
    numbers = list(range(lim + 1))
    ans = 0

    #Solve the problem
    for n in numbers:
        sqrtn = str(d.Decimal(n).sqrt())
        t = frac.Fraction(sqrtn).limit_denominator(bound)
        if t._denominator == 1: continue
        ans += t._denominator
        
    ans = str(ans)
    lim = str(lim)
    bound = str(bound)

    #Print the results
    print('The sum of all denominators of the best approximations to rad(n) ')
    print('for the denominator bound ' + bound + ', where n is not a ')
    print('perfect square and 1 < n <= ' + lim + ', is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**5
bounc = 10**12
solve(lim, bound)
