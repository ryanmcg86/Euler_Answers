'''Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors. 
For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
Link: https://projecteuler.net/problem=179'''

#Imports
import time

#Build a findDivisors function
def findDivisors(n):
    div = [0 for i in range(n)]
    for i in range(2, n // 2):
        for j in range(i * 2, n, i):
            div[j] += 1
    return div

#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    divs = findDivisors(limit)[2:]
    ans = 0

    #Solve the problem
    for i in range(len(divs) - 1):
        if divs[i] == divs[i + 1]:
            ans += 1
            
    ans = str(ans)
    lim = str(limit)
        
    #Print the results
    print 'The number of integers 1 < n < ' + lim + ', for which n and '
    print 'n + 1 have the same number of positive divisors, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**7
solve(limit)
