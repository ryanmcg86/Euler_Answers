'''Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. 
And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
Link: https://projecteuler.net/problem=120'''

#Imports
import time

#Build a solve function
def solve(n):
    #Declare variables
    start = time.time()
    
    #Solve the problem
    ans1 = int(((8 * n**3) - (6 * n**2) - (14 * n) + 3) / 24.)
    ans2 = (-1)**n
    ans3 = int(((2 * n) + 1) / 8.)
	
    ans = ans1 - (ans2 * ans3)
                
    #Print the results
    print 'The sum of the maximum remainders between 3 and ' + str(n)
    print 'for the given equation is ' + str(ans) + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 10**3
solve(n)
