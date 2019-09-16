'''How many 20 digit numbers n (without any leading zero) exist such 
that no three consecutive digits of n have a sum greater than 9?
Link: https://projecteuler.net/problem=164'''

#Imports
import time
   
#Build a Solve function
def solve(n, nmax):
    #Define variables
    start = time.time()
    count = [[1 for a in range(10)] for b in range(10)]
    ans = 0
    
    #Solve the problem
    for i in range(n - 2):
        tempCount = [[0 for j in range(10)] for k in range(10)]
        for b in range(10):
            for a in range(10):
                s = 0
                for c in range(10):
                    if a + b + c <= nmax:
                        s += count[b][c]
                tempCount[a][b] = s
        count = tempCount
	
    ans = str(sum(count[a][b] for a in range(1, 10) for b in range(10)))
    n = str(n)
    mx = str(nmax)

    #Print the results
    print 'There are ' + ans + ' ' + n + '-digit numbers n '
    print '(without any leading zero) which exist such that '
    print 'no 3 consecutive digits of n have a sum greater than ' + mx + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 20
nmax = 9
solve(n, nmax)
