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
        a = (n - 1) * n**(i - 1)
        b = (3 * n - 7) * (n - 2)**(i - 1)
        c = ((3 * n - 5) * (n - 1)**(i - 1) + (n - 3)**i)
        ans += a + b - c
        
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
