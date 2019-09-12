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
    
    #Solve the problem
    for i in range(n - 2):
		    count = {(a, b): sum(count[(b, c)] for c in range(10) if a + b + c <= 9) for a in range(10) for b in range(10)}
	
    ans = str(sum(count[(a, b)] for a in range(1, 10) for b in range(10)))
    n = str(n)
        
    #Print the results
    print 'There are ' + ans + ' ' + n + '-digit numbers n '
    print '(without any leading zero) which exist such that '
    print 'no 3 consecutive digits of n have a sum greater than 9.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 20
solve(n)
