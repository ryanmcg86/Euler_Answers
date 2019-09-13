'''How many 20 digit numbers n (without any leading zero) exist such 
that no three consecutive digits of n have a sum greater than 9?
Link: https://projecteuler.net/problem=164'''

#Imports
import time
   
#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    count = {(a, b): 1 for a in range(10) for b in range(10)}
    ans = 0
    
    #Solve the problem
    for i in range(n - 2):
        tempCount = {}
	for b in range(10):
	    for a in range(10):
                s = 0
		for c in range(10):
                    if a + b + c <= 9:
                        s += count[(b, c)]
                tempCount.update({(a, b): s})
        count = tempCount
		
    for a in range(1, 10):
        for b in range(10):
            ans += count[(a, b)]
    ans = str(ans)
    n = str(n)
        
    #Print the results
    print 'There are ' + ans + ' ' + n + '-digit numbers n '
    print '(without any leading zero) which exist such that '
    print 'no 3 consecutive digits of n have a sum greater than 9.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 20
solve(n)
