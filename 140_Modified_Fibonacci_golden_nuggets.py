'''Consider the infinite polynomial series AG(x) = xG1 + x2G2 + x3G3 + ..., 
where Gk is the kth term of the second order recurrence relation Gk = Gk−1 + Gk−2, G1 = 1 and G2 = 4; 
that is, 1, 4, 5, 9, 14, 23, ... .

For this problem we shall be concerned with values of x for which AG(x) is a positive integer.

The corresponding values of x for the first five natural numbers are shown below.

x                 AG(x)
(√5 − 1) / 4      1
2 / 5	            2
(√22 − 2) / 6     3
(√137 − 5) / 14   4
1 / 2             5
We shall call AG(x) a golden nugget if x is rational, because they become increasingly rarer; 
for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.
Link: https://projecteuler.net/problem=140'''

#Imports
import time
    
#Build a Solve function
def solve(nugget):
    #Define variables
    start = time.time()
    nuggets = {}
    bases = [[0, -1], [0, 1], [-3, -2], [-3, 2], [-4, -5], [2, 7]]
    a, b, c, d, e, f = -9, -4, -14, -20, -9, -28
    
    #Solve the problem
    for i in bases:
        x, y = i[0], i[1]
        for j in range(nugget):
            if x > 0:
                nuggets[x] = y
            xn = x
            yn = y
            x = a * xn + b * yn + c
            y = d * xn + e * yn + f
	
    ans = str(sum(sorted(nuggets)[:nugget]))
    nug = str(nugget)
    
    #Print the results
    print 'The sum of the first ' + nug + ' golden nuggests is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
nugget = 30
solve(nugget)
