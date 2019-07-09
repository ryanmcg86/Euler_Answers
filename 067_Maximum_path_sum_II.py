'''By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, as there are 2^99 altogether! 
If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
Link: https://projecteuler.net/project/resources/p067_triangle.txt
Link: https://projecteuler.net/problem=67'''

#Imports
import time

#Build find-maximum-path function
def findMaxPath(triangle):
    tri = triangle
    for i in range(len(tri) - 1, 0, -1):
        for j in range(len(tri[i]) - 1, 0, -1):
            left = tri[i][j - 1]
            right = tri[i][j]
            peak = tri[i - 1][j - 1]
            if left + peak > right + peak:
                tri[i - 1][j - 1] = left + peak
            else:
                tri[i - 1][j - 1] = right + peak
    return int(tri[0][0])
    
#Build a prep the triangle function
def prep(filename):
    f = open(filename, 'r')
    triangles = f.read().split('\n')
    triangles = triangles[0:len(triangles) - 1]
    
    for i in range(0, len(triangles)):
        triangles[i] = triangles[i].split(' ')
        
    for i in range(0, len(triangles)):
        for j in range(0, len(triangles[i])):
            triangles[i][j] = int(triangles[i][j])
            
    return triangles

#Solution function
def Solution(triangle):
    start = time.time()
    ans = str(findMaxPath(triangle))
    print 'The maximum total from top to bottom of the given triangle is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'triangles.txt'
triangle = prep(filename)
Solution(triangle)
