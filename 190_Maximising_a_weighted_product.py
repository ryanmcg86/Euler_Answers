'''Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with x1 + x2 + ... + xm = m 
for which Pm = x1 * x2^2 * ... * xm^m is maximised.

For example, it can be verified that [P10] = 4112 ([ ] is the integer part function).

Find Σ[Pm] for 2 ≤ m ≤ 15.
Link: https://projecteuler.net/problem=190'''

#Imports
import time

#Build the P function
def P(m):
    k = 2.0 / (m + 1)
    pm = 1
    for i in range(1, m + 1):
        pm *= (i * k)**i
    return int(pm)

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()

    #Solve the problem
    ans = str(sum(P(m) for m in range(2, lim + 1)))
    
    lim = str(lim)

    #Print the results
    print('The sum of P(m) from 2 to ' + lim + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 15
solve(lim)
