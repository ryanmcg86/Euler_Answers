'''For two positive integers a and b, the Ulam sequence U(a,b) is defined by U(a,b)1 = a, U(a,b)2 = b and for k > 2, 
U(a,b)k is the smallest integer greater than U(a,b)(k-1) which can be written in exactly one way as the sum of two 
distinct previous members of U(a,b).

For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the sum of two previous members, 
likewise 7 = 1 + 6 = 3 + 4.

Find ∑U(2,2n+1)k for 2 ≤ n ≤10, where k = 1011.
Link: https://projecteuler.net/problem=167'''

#Imports
import time
from itertools import izip, count
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    N = 32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152
    D = 126, 126, 1778, 6510, 23622, 510, 507842, 1523526, 8388606
    z = limit - 3
    t = 0
    
    #Solve the problem
    for v, n, d in izip(xrange(5, 22, 2), N, D):
        l = [0] * n
        for s, x in izip(count(), ulam2_2(v)):
            if x - l[s % n] == d and not (z - s - 1) % n:
                t += x + d * (z - s - 1) / n
                break
            l[s % n] = x
    
    t = str(t)
    lim = str(limit)

    #Print the results
    print 'When k = ' + lim + ', the sum of U(2, 2n + 1) '
    print 'sub k for 2 <= n <= 10, is ' + t + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**11
solve(limit)
