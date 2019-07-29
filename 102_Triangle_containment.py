'''Three distinct points are plotted at random on a Cartesian plane, 
for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing 
the co-ordinates of one thousand "random" triangles, find the number of triangles for which 
the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
Link: https://projecteuler.net/problem=102'''

#Imports
import time

#Build an area function
def area(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3)
    b = x2 * (y3 - y1)
    c = x3 * (y1 - y2)
    return abs((a + b + c) / 2.)

#Build a solve function
def solve(filename):
    #Define variables
    start = time.time()
    f = open(filename, 'r')
    tris = f.read().split('\n')
    tris = tris[0 : len(tris) - 1]    #Remove the trailing '' at the end of the list
    ans = 0

    for i in range(0, len(tris)):     #Split the list by commas
        tris[i] = tris[i].split(',')

    for i in range(0, len(tris)):     #Convert all the entries from strings to ints
        for j in range(0, len(tris[i])):
            tris[i][j] = int(tris[i][j])
    
    #Solve the problem
    #Find the areas of the sub triangles, if they sum up
    #to the area of the whole triangle, then the origin 
    #is within the triangle
    for a, b, c, d, e, f in tris:
        pab = area(0, 0, a, b, c, d)
        pbc = area(0, 0, c, d, e, f)
        pac = area(0, 0, a, b, e, f)
        if pab + pbc + pac == area(a, b, c, d, e, f):
            ans += 1
    
    #Print the results
    print 'Using ' + filename + ', the number of triangles '
    print 'for which the interior contains the origin is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'p102_triangles.txt'
solve(filename)
