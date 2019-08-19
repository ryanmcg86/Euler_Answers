'''Let ABC be a triangle with all interior angles being less than 120 degrees. 
Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC are constructed on each side of triangle ABC, 
the circumscribed circles of AOB, BNC, and AMC will intersect at a single point, T, inside the triangle. 
Moreover he proved that T, called the Torricelli/Fermat point, minimises p + q + r. 
Even more remarkable, it can be shown that when the sum is minimised, AN = BM = CO = p + q + r and that AN, 
BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall call triangle ABC a Torricelli triangle. 
For example, a = 399, b = 455, c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli triangles.
Link: https://projecteuler.net/problem=143'''

#Imports
import time
    
#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    D = {}
    pqr = set()
    
    #Solve the problem
    for m in range(2, int(limit**0.5) + 1):
        for n in range(1, m):
            if gcd(m, n) > 1 or (m - n) % 3 == 0:
                continue
            p = 2 * m * n + n * n
            q = m * m - n * n
            k = 1
            while k * (p + q) < limit:
                if k * q in D:
                    D[k * q].append(k * p)
                else:
                    D[k * q] = [k * p]
                if k * p in D:
                    D[k * p].append(k * q)
                else:
                    D[k * p] = [k * q]
                k += 1
	
    for p in D.keys():
        for q in sorted(D[p], reverse = True):
            for r in D[p][D[p].index(q):]:
                if q in D and r in D[q]:
                    if p + q + r > limit:
                        continue
                    else:
                        pqr.add(p + q + r)
	
    ans = str(sum(pqr))
    lim = str(limit)
    
    #Print the results
    print 'The sum of all distinct values of p + q + r '
    print '<= ' + lim + ' for Torricelli triangles is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 12 * 10**4
solve(limit)
