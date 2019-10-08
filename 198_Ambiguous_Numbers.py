'''A best approximation to a real number x for the denominator bound d is a rational number rs (in reduced form) with s ≤ d, 
so that any rational number pq which is closer to x than rs has q>d.

Usually the best approximation to a real number is uniquely determined for all denominator bounds. 
However, there are some exceptions, e.g. 940 has the two best approximations 14 and 15 for the denominator bound 6. 
We shall call a real number x ambiguous, if there is at least one denominator bound for which x possesses two best approximations. 
Clearly, an ambiguous number is necessarily rational.

How many ambiguous numbers x = p / q, 0 < x < 1 / 100, are there whose denominator q does not exceed 10^8?
Link: https://projecteuler.net/problem=198'''

#Imports
import time

#Build a Solve function
def solve(lim, qlim):
    #Define variables
    start = time.time()
    lim2 = lim / 2
    stack = []
    count = 0
  
    #Solve the problem
    for a in range(qlim, int(lim2**0.5)):
        stack.append((a, a + 1))
        while stack:
            a, b = stack.pop()
            if a * b <= lim2:
                count += 1
                c = a + b
                stack.append((a, c))
                stack.append((c, b))
                
    ans = str(int(count + lim2 - qlim / 2))
    lim, qlim = str(lim), str(qlim)
    rang = '0 < x < 1 / ' + qlim

    #Print the results
    print('There are ' + ans + ' ambiguous numbers ')
    print('x = p / q, ' + rang + ', whose ')
    print('denominator q does not exceed ' + lim + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**8
qlim = 100
solve(lim, qlim)
