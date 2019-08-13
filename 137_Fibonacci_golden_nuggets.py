'''Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., 
where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; 
that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly AF(1/2)	 = 	(1/2) * 1 + (1/2)^2 * 1 + (1/2)^3 * 2 + (1/2)^4 * 3 + (1/2)^5 * 5 + ...
 	 = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 	 = 	2
The corresponding values of x for the first five natural numbers are shown below.

x                AF(x)
√2 − 1           1
1/2              2
(√13 − 2) / 3    3
(√89 − 5) / 8    4
(√34 − 3) / 5    5
We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; for example, 
the 10th golden nugget is 74049690.

Find the 15th golden nugget.
Link: https://projecteuler.net/problem=137'''

#Imports
import time

#Build a build suffix function
def buildSuffix(num):
    suffs = ['th', 'st', 'nd', 'rd']
    suff = suffs[0]
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        lastdigit = int(str(num)[-1])
        if lastdigit < len(suffs):
            suff = suffs[lastdigit]
    return suff
    
#Build a Solve function
def solve(nugget):
    #Define variables
    start = time.time()
    f1, f2 = 1, 1
    
    #Solve the problem
    for i in range(2 * nugget - 1):
        f1temp = f1
        f1 = f2
        f2 += f1temp
        
    ans = str(f1 * f2)
    nugget = str(nugget) + buildSuffix(nugget)
    
    #Print the results
    print 'The ' + nugget + ' golden nugget is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
nugget = 15
solve(nugget)
