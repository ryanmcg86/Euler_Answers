'''Starting from zero the natural numbers are written down in base 10 like this: 
0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n, we will update the number of ones 
that have occurred and call this number f(n,1). The first values for f(n,1), then, are as follows:

n     f(n,1)
0     0
1     1
2     1
3     1
4     1
5     1
6     1
7     1
8     1
9     1
10    2
11    4
12    5
Note that f(n,1) never equals 3. 
So the first two solutions of the equation f(n,1) = n are n = 0 and n = 1. The next solution is n = 199981.

In the same manner the function f(n,d) gives the total number of digits d that have been written down after 
the number n has been written. 
In fact, for every digit d ≠ 0, 0 is the first solution of the equation f(n,d) = n.

Let s(d) be the sum of all the solutions for which f(n,d) = n. 
You are given that s(1) = 22786974071.

Find ∑ s(d) for 1 ≤ d ≤ 9.

Note: if, for some n, f(n,d) = n for more than one value of d this value of n is counted again for every value 
of d for which f(n,d) = n.
Link: https://projecteuler.net/problem=156'''

#Imports
import time

#Build a calc function
def calc(n, d):
    n += 1
    ret = 0
    powp = 1
    while powp < n:
        c = n / powp % 10
        ret += n / powp / 10 * powp
        if c == d:
            ret += n % (10 * powp) - d * powp
        elif c > d:
            ret += powp
        powp *= 10
    return ret
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = {'y': 0}
    
    #Solve the problem
    def dfs(digit, n, powp):
        lo = calc(n, digit)
        hi = calc(n + powp, digit)
        if hi < n or lo > n + powp:
            return
        if powp == 1:
            if lo == n:
                d = str(digit) + ': ' + str(n)
                print 'find one solution for d = ' + d
                ans['y'] += n
            return
        powp /= 10
        for i in range(10):
            dfs(digit, n + i * powp, powp)
            
    for i in range(1, 10):
        dfs(i, 0, limit)

    ans = str(ans['y'])
    
    #Print the results
    print 'The sum of s(d) for 1 <= d <= 9 is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**15
solve(limit)
