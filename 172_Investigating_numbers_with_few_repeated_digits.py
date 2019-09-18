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
    for a1 in range(11):
        for a2 in range(10):
            for a3 in range(7):
                if a1 + 2 * a2 + 3 * a3 == n:
                    if a1 + a2 + a3 <= 10:
                        z = fact(n)
                        y = 6**a3
                        x = 2**a2
                        w = fact(a3)
                        v = fact(a2)
                        u = fact(a1)
                        np = z / y / x / w / v / u
                        t = fact(10)
                        s = fact(10 - a1 - a2 - a3)
                        ans += t / s * np
	
    ans = str(int(ans * 9 / 10))
    n = str(n)

    #Print the results
    print 'There are ' + ans + ' ' + n + '-digit '
    print 'numbers n (without leading zeros) such that '
    print 'no digit occurs more than three times in n.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 18
solve(n)
