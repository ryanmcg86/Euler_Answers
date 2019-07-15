'''It turns out that 12 cm is the smallest length of wire that can be bent 
to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
sided right angle triangle, and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can 
exactly one integer sided right angle triangle be formed?
Link: https://projecteuler.net/problem=75'''

#Imports
import time

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x

#Build a solve function
def solve(limit):
    #Define variables
    start  = time.time()
    yes    = set()
    no     = set()
    mlimit = int((limit / 2)**0.5)
    
    #Solve the problem
    for m in range(2, mlimit):
        for n in range(m - 1, 0, -2):
            if gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                p = a + b + c
                for k in range(1, (limit / p) + 1):
                    tri = k * p
                    if tri in yes:
                        no.add(tri)
                    else:
                        yes.add(tri)

    ans = str(len(yes) - len(no))

    #Print the results
    print 'For length L <= ' + str(limit) + ', there are ' + ans + ' values where '
    print 'exactly one integer sided right triangle can be formed.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 1500000
solve(limit)
