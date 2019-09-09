'''In the hexadecimal number system numbers are represented using 16 different digits:

0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with all of the 
digits 0,1, and A present at least once?
Give your answer as a hexadecimal number.

(A,B,C,D,E and F in upper case, without any leading or trailing code that marks the number as 
hexadecimal and without leading zeroes , e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
Link: https://projecteuler.net/problem=162'''

#Imports
import time
   
#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for i in range(1, n + 1):
        i1, n1, n2, n3 = i - 1, n - 1, n - 2, n - 3
        tot  = n1  * n**i1       #Total number of numbers
	t01a = tot - n3**i       #number of numbers with 0, 1, or A
	t0a  = tot - n2**i       #number of numbers with 0 or A
	t01  = tot - n2**i       #number of numbers with 0 or 1
	t1a  = tot - n2**i1 * n3 #number of numbers with 1 or A
	t0   = tot - n1**i       #number of numbers with 0
	t1   = tot - n1**i1 * n2 #number of numbers with 1
	ta   = tot - n1**i1 * n2 #number of numbers with A
	ans += t01a - t0a - t01 - t1a + t0 + t1 + ta
        
    ans = str(hex(ans))[2:len(str(hex(ans))) - 1].upper()
    lim = str(n)
        
    #Print the results
    print 'In hexidecimal, there are ' + ans + ' numbers '
    print 'containing at most ' + lim + ' hexidecimal digits with '
    print 'all of the digits 0, 1, and A present at least once.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 16
solve(n)
