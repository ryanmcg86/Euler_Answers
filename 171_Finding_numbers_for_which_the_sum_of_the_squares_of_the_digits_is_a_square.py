'''For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.

f(3) = 32 = 9,
f(25) = 22 + 52 = 4 + 25 = 29,
f(442) = 42 + 42 + 22 = 16 + 16 + 4 = 36

Find the last nine digits of the sum of all n, 0 < n < 10^20, such that f(n) is a perfect square.
Link: https://projecteuler.net/problem=171'''

#Imports
import time

#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    length = 20
    base = 10
    modulus = 10**9
	
    msds = (base - 1)**2 * length #maximum square digit sum
    sqsum = []
    count = []
    
    #Solve the problem
    for i in range(length + 1):
        sqsum.append([0] * (msds + 1))
        count.append([0] * (msds + 1))
        if i == 0: count[0][0] = 1
        else:
            for j in range(base):
                k = 0
                index = k + j**2
                while index <= msds
                    a = sqsum[i][index]
                    b = sqsum[i - 1][k]
                    c = pow(base, i - 1, modulus) * j * count[i - 1][k]
                    d = count[i][index]
                    e = count[i - 1][k]
                    
                    sqsum[i][index] = (a + b + c) % modulus
                    count[i][index] = (d + e) % modulus
                    
                    k += 1
                    index = k + j**2
	
    ans = sum(sqsum[length][i**2] for i in range(1, int((msds)**0.5) + 1))
    ans = str(ans)[-9:]

    #Print the results
    print 'The last nine digits of the sum of all n, 0 < n < 10^20, '
    print 'such that f(n) is a perfect square are ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
