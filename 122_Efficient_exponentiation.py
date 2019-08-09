'''The most naive way of computing n^15 requires fourteen multiplications:

n × n × ... × n = n^15

But using a "binary" method you can compute it in six multiplications:

n × n = n^2
n^2 × n^2 = n^4
n^4 × n^4 = n^8
n^8 × n^4 = n^12
n^12 × n^2 = n^14
n^14 × n = n^15

However it is yet possible to compute it in only five multiplications:

n × n = n^2
n^2 × n = n^3
n^3 × n^3 = n^6
n^6 × n^6 = n^12
n^12 × ^n3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute n^k; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
Link: https://projecteuler.net/problem=122'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Declare variables
    start = time.time()
    routeMaps    = [0] * (limit + 1)
    routeMaps[1] = list([set([1])])
    mins         = [float('inf')] * (limit + 1)
    mins[1]      = 0
    
    #Solve the problem
    for n in range(2, limit + 1):
        for i in range((n + 1) / 2, n):
            for routeSet in routeMaps[i]:
                if mins[n] >= mins[i] + 1:
                    if n - i in routeSet:
                        if mins[n] > mins[i] + 1:
                            mins[n] = mins[i] + 1
                            routeMaps[n] = list([set([n]) | routeSet])
                        else:
                            routeMaps[n].append(set([n]) | routeSet)

    ans = str(sum([mins[i] for i in range(1, len(mins))]))
        
    #Print the results
    print 'The sum of the minimum number of multiplications '
    print 'to compute n^k for 1 <= k <= ' + str(limit) + ' is ' + ans + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 200
solve(limit)
