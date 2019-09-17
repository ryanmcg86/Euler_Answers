'''A segment is uniquely defined by its two endpoints.
By considering two line segments in plane geometry there are three possibilities:
the segments have zero points, one point, or infinitely many points in common.

Moreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of 
either one of the segments or of both. If a common point of two segments is not an endpoint of either of the segments it 
is an interior point of both segments.
We will call a common point T of two segments L1 and L2 a true intersection point of L1 and L2 if T is the only common point 
of L1 and L2 and T is an interior point of both segments.

Consider the three segments L1, L2, and L3:

L1: (27, 44) to (12, 32)
L2: (46, 53) to (17, 62)
L3: (46, 70) to (22, 40)

It can be verified that line segments L2 and L3 have a true intersection point. We note that as the one of the end points of 
L3: (22,40) lies on L1 this is not considered to be a true point of intersection. L1 and L2 have no common point. So among 
the three line segments, we find one true intersection point.

Now let us do the same for 5000 line segments. To this end, we generate 20000 numbers using the so-called "Blum Blum Shub" 
pseudo-random number generator.

    s0 = 290797

    sn+1 = sn×sn (modulo 50515093)

    tn = sn (modulo 500)

To create each line segment, we use four consecutive numbers tn. That is, the first line segment is given by:

(t1, t2) to (t3, t4)

The first four numbers computed according to the above generator should be: 27, 144, 12 and 232. The first segment would 
thus be (27,144) to (12,232).

How many distinct true intersection points are found among the 5000 line segments?
Link: https://projecteuler.net/problem=165'''

#Imports
import time

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x

#Build an intersect function
def intersect(seg1, seg2):
    dx1 = seg1[2] - seg1[0]
    dy1 = seg1[3] - seg1[1]
    dx2 = seg2[2] - seg2[0]
    dy2 = seg2[3] - seg2[1]
    denom = dx1 * dy2 - dy1 * dx2
    if denom == 0: return None
    if denom < 0:
        (sn, denom) = (-1, -denom)
    else:
        sn = 1
    t = sn * (dy2 * (seg2[0] - seg1[0]) - dx2 * (seg2[1] - seg1[1]))
    if t <= 0 or t >= denom: return None
    s = sn * (dy1 * (seg2[0] - seg1[0]) - dx1 * (seg2[1] - seg1[1]))
    if s <= 0 or s >= denom: return None
    return (seg1[0] * denom + dx1 * t, seg1[1] * denom + dy1 * t, denom)
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    s = 290797
    bbs = []
    for i in range(limit):
        t = []
        for j in range(4):
            s = (s * s) % 50515093
            t.append(int(s % 500))
        bbs.append(tuple(t))
    pts = []
    
    #Solve the problem
    for i in range(limit):
        for j in range(i + 1, limit):
            t = intersect(bbs[i], bbs[j])
            if t:
                g0 = gcd(t[0], t[2])
                g1 = gcd(t[1], t[2])
                t0g0 = t[0] / g0
                t2g0 = t[2] / g0
                t1g1 = t[1] / g1
                t2g1 = t[2] / g1
                pts.append((t0g0, t2g0, t1g1, t2g1))
    
    total = str(len(pts))
    ans = str(len(set(pts)))

    #Print the results
    print 'The total amount of intersections is ' + total + '.'
    print 'The amount of unique intersections is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 5000
solve(limit)
