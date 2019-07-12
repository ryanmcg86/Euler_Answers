'''Consider the fraction, n/d, where n and d are positive integers. 
If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
Link: https://projecteuler.net/problem=72'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    phi = [0, 0]
    ans = 0
    
    #Solve the problem
    for i in range(2, limit + 1):
        phi.append(i)

    for i in range(2, limit + 1):
        if phi[i] == i:
            for m in range(i, limit + 1, i):
                phi[m] = phi[m] - phi[m] / i
            
    for i in range(2, limit + 1):
        ans += phi[i]

    #Print the results
    print 'For d <= ' + str(limit) + ', ' + str(ans) + ' elements would '
    print 'be contained in the set of proper fractions.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 10**6
solve(limit)
