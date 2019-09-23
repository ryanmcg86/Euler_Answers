'''Let ABCD be a convex quadrilateral, with diagonals AC and BD. At each vertex the diagonal makes an angle 
with each of the two sides, creating eight corner angles.

                              D---------C
                              |  \    /  \ 
                               |   \ /    \
                               |   /  \    \ 
                                | /     \   \
                                A------------B


For example, at vertex A, the two angles are CAD, CAB.

We call such a quadrilateral for which all eight corner angles have integer values when measured in degrees 
an "integer angled quadrilateral". An example of an integer angled quadrilateral is a square, where all eight 
corner angles are 45°. Another example is given by DAC = 20°, BAC = 60°, ABD = 50°, CBD = 30°, BCA = 40°, 
DCA = 30°, CDB = 80°, ADB = 50°.

What is the total number of non-similar integer angled quadrilaterals?

Note: In your calculations you may assume that a calculated angle is integral if it is within a tolerance of 
10^-9 of an integer value.
Link: https://projecteuler.net/problem=177'''

#Imports
import time
from math import sin,cos,atan,degrees,radians

#Build an isInteger function
def isInteger(x):
    return abs(round(x) - x) < 10**(-8)

#Build a lexicografic order for pairs function
def compare0(x, y):
    for i in range(2):
        if x[i] > y[i]:
            return 1
        elif x[i] < y[i]:
            return -1
    return 0

#Build a lexicografic order for list of pairs function
def compare(x, y):
    for i in range(4):
        if compare0(x[i], y[i]) == 1:
            return 1
        elif compare0(x[i], y[i]) == -1:
            return -1
    return 0

#Build a reversed quadrilateral function
def mirror(xs):
    (a1, b1), (a2, b2), (a3, b3), (a4, b4) = xs
    return (b4, a4), (b3, a3), (b2, a2), (b1, a1)

#Build a similar quadrilaterals by rotation function
def cycle(xs):
    res = []
    for i in range(1, len(xs)):
        res.append(xs[i:] + xs[:i])
    return res

#Build a get all similar quadrilaterals function
def transform(xs):
    ys = mirror(xs)
    return cycle(xs) + [ys] + cycle(ys)

#Build a by lexicographic order xs is before the other similar quadrilaterals
def unique(xs):
    return all(compare(xs, txs) < 1 for txs in transform(xs))

#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    s     = [sin(radians(x)) for x in range(180)]
    c     = [cos(radians(x)) for x in range(180)]
    a1    = 1
    step  = 1
    count = 0

    #Solve the problem
    while a1 <= 45:
        b1 = a1
        while a1 + b1 < 180:
            a2 = a1
            while 2 * a1 + b1 + a2 <= 180:
                b2 = 180 - a1 - b1 - a2
                a3 = a1
                while a1 + a2 + b2 + a3 <= 180:
                    b3 = 180 - a2 - b2 - a3
                    p3 = s[a1] * s[a2] * s[a3]
                    q3 = s[b1] * s[b2] * s[b3]
                    den = p3 - q3 * c[a1 + b1]
                    if den == 0:
                        a4 = 90
                    else:
                        t4 = q3 * s[a1 + b1] / den
                        if t4 > 0:
                            a4 = degrees(atan(t4))
                        else:
                            a4 = 180 - degrees(atan(abs(t4)))
                    if isInteger(a4):
                        a4 = int(a4 + 0.5)
                        b4 = a2 + b2 - a4
                        ab1 = (a1, b1)
                        ab2 = (a2, b2)
                        ab3 = (a3, b3)
                        ab4 = (a4, b4)
                        t = (ab1, ab2, ab3, ab4)
                        if unique(t):
                            count += 1
                    a3 += step
                a2 += step       
            b1 += step
        a1 += step
        
    ans = str(count)
        
    #Print the results
    print 'The total number of non-similar integer '
    print 'angled quadrilaterals is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
