'''A robot moves in a series of one-fifth circular arcs (72°), with a free choice of a clockwise or an 
anticlockwise arc for each step, but no turning on the spot.

When there are 25 arcs, there are 70932 possible closed paths.

Given that the robot starts facing North, how many journeys of 70 arcs in length can it take that return it, 
after the final arc, to its starting position?
(Any arc may be traversed multiple times.)
Link: https://projecteuler.net/problem=208'''

#Imports
import time

#Build a Solve function
def solve(arcs):
    #Define variables
    start = time.time()
    walks = int(360 / 72)
    m     = int(arcs / walks)
    c     = [[0 for i in range(m + 1)] for j in range(m + 1)]
    ans   = 0
    
    for i in range(1, m + 1):
        c[i][0] = 1
        c[i][i] = 1
    for i in range(1, m + 1):
        for j in range(1, i):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

    #Solve the problem
    for n in range(m):
        m1, n1 = m - 1, n - 1
        ans += pow(c[m1][n], walks)
        if n > 0:
            a, b = c[m1][n], c[m1][n1]
            for i in range(1, walks):
                ans += pow(a, walks - i) * pow(b, i)
                
    ans = str(ans * 2)
    arc = str(arcs)

    #Print the results
    print('Given that the robot starts facing North, it can ')
    print('take ' + ans + ' journeys of ' + arc + ' arcs in length that ')
    print('return it, after the final arc, to its starting position.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
arcs = 70
solve(arcs)
