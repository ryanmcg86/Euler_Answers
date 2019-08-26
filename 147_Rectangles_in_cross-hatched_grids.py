'''In a 3x2 cross-hatched grid, a total of 37 different rectangles could be situated within that grid.

There are 5 grids smaller than 3x2, vertical and horizontal dimensions being important, 
i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following number of different rectangles 
could be situated within those smaller grids:

1x1	1
2x1	4
3x1	8
1x2	4
2x2	18
Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller grids?
Link: https://projecteuler.net/problem=147'''

#Imports
import time
    
#Build a rect function
def rect(m, n):
    if m < n:
        x = m
        m = n
        n = x
    hvr = m * (m + 1) * n * (n + 1) / 4
    dag = n * ((2 * m - n) * (4 * n**2 - 1) - 3) / 6
    return hvr + dag
    
#Build a Solve function
def solve(w, h):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for m in range(1, w + 1):
        for n in range(1, h + 1):
            ans += rect(m, n)

    a = str(ans)
    g = str(w) + 'x' + str(h)

    #Print the results
    print 'You can fit ' + a + ' different rectangles in a ' + g + ' grid.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
w = 47
h = 43
solve(w, h)
