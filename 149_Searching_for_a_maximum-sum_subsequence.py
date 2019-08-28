'''Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers 
in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

−2  5  3  2
 9 −6  5  1
 3  2  7  3
−1  8 −4  8

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, s[k] = [100003 − 200003 * k + 300007 * k^3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [s[k−24] + s[k−55] + 1000000] (modulo 1000000) − 500000.

Thus, s[10] = −393027 and s[100] = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the first row (sequentially), 
the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
Link: https://projecteuler.net/problem=149'''

#Imports
import time

#Build a Solve function
def solve(size):
    #Define variables
    start = time.time()
    s = []
    
    #Solve the problem
    for i in range(size**2):
        k = i + 1
        if k <= 55:
            one = 100003 - 200003 * k + 300007 * k**3
            s.append(one % 10**6 - 5 * 10**5)
        else:
            s.append((s[-24] + s[-55]) % 10**6 - 5 * 10**5)
            
    grid = [s[i * size : (i + 1) * size] for i in range(size)]
    
    def gm(x, y, dx, dy):
        result = 0
        current = 0
        while 0 <= x < size and 0 <= y < size:
            current = max(current + grid[y][x], 0)
            result  = max(current, result)
            x += dx
            y += dy
        return result
        
    ans = str(max(max(gm(0, i, 1, 0),
                      gm(i, 0, 0, 1),
                      gm(0, i, 1, 1),
                      gm(i, 0, 1, 1),
                      gm(i, 0, -1, 1),
                      gm(size - 1, i, -1, 1)) for i in range(size)))
                      
    g = str(size) + ' x ' + str(size)

    #Print the results
    print 'Using a Lagged Fibonacci Generator to generate a '
    print g + ' grid, the greatest sum of (any number '
    print 'of) adjacent entries in any direction (horizontal, '
    print 'vertical, diagonal or anti-diagonal) is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
size = 2000
solve(size)
