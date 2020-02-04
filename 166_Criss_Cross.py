'''A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, 
each column, and both diagonals have the same sum?
Link: https://projecteuler.net/problem=166'''

#Imports
import time

#Build a quad function
def quad():
    for i in range(10):
        for j in range(10):
            s = i + j
            for k in range(min(s + 1, 10)):
                if s - k < 10:
                    yield i, j, k, s - k

#Build a pair function
def pair(n):
    if n < 10:
        for i in range(n + 1):
            yield i, n - i
    else:
        for x, y in pair(18 - n):
            yield 9 - x, 9 - y
   
#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    count = 0
    
    #Solve the problem
    for d1, d4, e2, e3 in quad():
        for e1, e4, d2, d3 in quad():
            s = d1 + d2 + d3 + d4
            c1 = 0
            for x, y in pair(s - d1 - e1):
                if 0 <= s - x - d2 - e3 <= 9:
                    if 0 <= s - y - e2 - d3 <= 9:
                        c1 += 1
            c2 = 0
            for x, y in pair(s - d1 - e4):
                if 0 <= s - x - d2 - e2 <= 9:
                    if 0 <= s - y - d3 - e3 <= 9:
                        c2 += 1
            count += c1 * c2
    
    ans = str(count)

    #Print the results
    print 'You can fill a 4 x 4 grid with the digits d, '
    print '0 <= d <= 9 so that each row, each column, and both '
    print 'diagonals have the same sum ' + ans + ' different ways.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
