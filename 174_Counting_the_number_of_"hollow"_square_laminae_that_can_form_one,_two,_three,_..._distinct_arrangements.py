'''We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses 
vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle. 
However, using thirty-two tiles it is possible to form two distinct laminae:

                 * * * * * *         * * * * * * * * *
                 * * * * * *         *               *
                 * *     * *         *               *
                 * *     * *         *               *
                 * * * * * *         *               *
                 * * * * * *         *               *
                                     *               *
                                     *               *
                                     * * * * * * * * *
                                     
If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).

Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example, N(15) = 832.

What is ∑ N(n) for 1 ≤ n ≤ 10?
Link: https://projecteuler.net/problem=174'''

#Imports
import time

#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    n = [0] * (limit + 1)

    #Solve the problem
    for i in range(1, limit / 4):
        nt = i * 4 + 4
        sumx = nt
        while sumx <= limit:
            n[sumx] += 1
            nt      += 8
            sumx    += nt

    ans = str(sum(1 <= i <= 10 for i in n))
    lim = str(limit)
        
    #Print the results
    print 'The sum of N(n) for 1 <= n <= 10, where '
    print 'N(n) is the number of t <= ' + lim + ' such '
    print 'that t is type L(n), where L(n) is the '
    print 'amount of types of laminae formed, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**6
solve(limit)
