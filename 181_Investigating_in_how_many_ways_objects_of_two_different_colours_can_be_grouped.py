'''Having three black objects B and one white object W they can be grouped in 7 ways like this:

(BBBW)	(B,BBW)	(B,B,BW)	(B,B,B,W)	(B,BB,W)	(BBB,W)	(BB,BW)
In how many ways can sixty black objects B and forty white objects W be thus grouped?
Link: https://projecteuler.net/problem=181'''

#Imports
import time

#Build a Solve function
def solve(m, n):
    #Define variables
    start = time.time()
    p = [[1] * (m + 1) for j in range(m + 1)]

    #Solve the problem
    for l in range(m + 1):
        for i in range(m + 1):
            if l + i > 1:
                for j in range(l, m + 1):
                    for k in range(i, m + 1):
                        p[j][k] += p[j - l][k - i]
                        
    ans = str(p[m][n])
    m = str(m)
    n = str(n)

    #Print the results
    print m + ' black objects B and ' + n + ' white objects W '
    print 'can be grouped in ' + ans + ' different ways.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
m, n = 60, 40
solve(m, n)
