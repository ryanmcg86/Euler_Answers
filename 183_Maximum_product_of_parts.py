'''Let N be a positive integer and let N be split into k equal parts, r = N / k, so that N = r + r + ... + r.
Let P be the product of these parts, P = r × r × ... × r = rk.

For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.

Let M(N) = Pmax for a given value of N.

It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which leads to Pmax = (11 / 4)^4; 
that is, M(11) = 14641 / 256 = 57.19140625, which is a terminating decimal.

However, for N = 8 the maximum is achieved by splitting it into three equal parts, so M(8) = 512 / 27, 
which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.

For example, ∑ D(N) for 5 ≤ N ≤ 100 is 2438.

Find ∑ D(N) for 5 ≤ N ≤ 10000.
Link: https://projecteuler.net/problem=183'''

#Imports
import time
import math

#Define the D function
def D(n):
    k = round(n / math.e)
    while k % 2 == 0: k /= 2
    while k % 5 == 0: k /= 5
    if n % k != 0: return n
    return n

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()

    #Solve the problem
    ans = str(sum(D(n) for n in range(5, lim + 1)))
    lim = str(lim)

    #Print the results
    print 'The sum of D(N) for 5 <= N <= ' + lim + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
lim = 10**4
solve(lim)
