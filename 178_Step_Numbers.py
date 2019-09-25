'''Consider the number 45656.
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 10^40 are there?
Link: https://projecteuler.net/problem=178'''

#Imports
import time

#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    s = [{} for n in range(limit)]
    s[0] = {(i, i, i): 1 for i in range(1, 10)}
    ans = 0

    #Solve the problem
    for n in range(1, limit):
        for ss in s[n - 1]:
            for d in (-1, 1):
                x = ss[0] + d
                if 0 <= x < 10:
                    y = (x, min(ss[1], x), max(ss[2], x))
                    if y in s[n]:
                        s[n][y] += s[n - 1][ss]
                    else:
                        s[n][y] = s[n - 1][ss]
                        
    for n in range(limit):
        for x in s[n]:
            if x[1] == 0 and x[2] == 9:
                ans += s[n][x]
                
    ans = str(ans)
    lim = str(limit)
        
    #Print the results
    print 'There are ' + ans + ' pandigital '
    print 'step numbers less than 10^' + lim + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 40
solve(limit)
