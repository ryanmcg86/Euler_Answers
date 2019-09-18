'''How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?
Link: https://projecteuler.net/problem=172'''

#Imports
import time

#Build a factorial function
def fact(n):
    return fact(n - 1) * n if n > 1 else 1

#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for a in range(n / 3 + 1):
        for b in range((n - 3 * a) / 2 + 1):
            c = n - 3 * a - 2 * b
            if a + b + c <= 10:
                z = 10 - a - b - c
                y = fact(n) / 6**a / 2**b
                k = fact(10) / fact(a) / fact(b) / fact(c) / fact(z) * y
                ans += k
	
    ans = str(ans * 9 / 10)
    n = str(n)

    #Print the results
    print 'There are ' + ans + ' ' + n + '-digit '
    print 'numbers n (without leading zeros) such that '
    print 'no digit occurs more than three times in n.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 18
solve(n)
