'''An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) }, 
consists of all points (X,Y,Z) such that x0 ≤ X ≤ x0+dx, y0 ≤ Y ≤ y0+dy and z0 ≤ Z ≤ z0+dz. 
The volume of the cuboid is the product, dx × dy × dz. 
The combined volume of a collection of cuboids is the volume of their union and will be less 
than the sum of the individual volumes if any cuboids overlap.

Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters

x0 = S6n-5 modulo 10000
y0 = S6n-4 modulo 10000
z0 = S6n-3 modulo 10000
dx = 1 + (S6n-2 modulo 399)
dy = 1 + (S6n-1 modulo 399)
dz = 1 + (S6n modulo 399)

where S1,...,S300000 come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3]   (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55]   (modulo 1000000)

Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.

The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.

What is the combined volume of all 50000 cuboids, C1,...,C50000 ?
Link: https://projecteuler.net/problem=212'''

#Imports
import time

#Build a get_intersections function
def get_intersections(cubes, inters):
    ret = []
    for i in range(len(inters)):
        a = inters[i]
        for j in range(a[9] + 1, len(cubes)):
            b = cubes[j]
            if cube_intersect(a, b):
                inter = get_intersection(a, b)
                inter[9] = j
                ret.append(inter)
            else:
                if a[6] < b[0]: break
    return ret

#Build a cube_sum function
def cube_sum(cubes):
    return sum(x[3] * x[4] * x[5] for x in cubes)

#Build a get_intersection function
def get_intersection(a, b):
    ans = []
    xyz = [max(a[i], b[i]) for i in range(3)]
    for i in range(3): ans.append(xyz[i])
    rxyz = [min(a[i], b[i]) for i in range(6, 9)]
    for i in range(3): ans.append(rxyz[i] - xyz[i])
    for i in range(3): ans.append(rxyz[i])
    ans.append(0)
    return ans

#Build a cube_intersect function
def cube_intersect(a, b):
    for i in range(3):
        if a[i + 6] < b[i] or b[i + 6] < a[i]: return False
    return True

#Build a Lagged Fibonacci Generator function
def lfg(target):
	fg = [0] * (6 * target + 1)
	for k in range(6 * target + 1):
		if k <= 55:
			fg[k] = (100003 - 200003 * k + 300007 * k**3) % 10**6
		else:
			fg[k] = (fg[k - 24] + fg[k - 55]) % 10**6
	return fg

#Build a Solve function
def solve(target):
    #Define variables
    start = time.time()
    fg = lfg(target)
    cubes = []
    m = -1

    #Solve the problem
    for i in range(target):
        n = 6 * (i + 1)
        x = fg[n - 5] % 10**4
        y = fg[n - 4] % 10**4
        z = fg[n - 3] % 10**4
        dx = 1 + fg[n - 2] % 399
        dy = 1 + fg[n - 1] % 399
        dz = 1 + fg[n]     % 399
        cubes.append([x, y, z, dx, dy, dz, x + dx, y + dy, z + dz, i])
        
    cubes = sorted(cubes, key = lambda x:(x[0], x[1], x[2]))
    
    for i in range(len(cubes)): cubes[i][9] = i
        
    s = cube_sum(cubes)
    inters = cubes[:]
    
    while len(inters) > 0:
        inters = get_intersections(cubes, inters)
        s += m * cube_sum(inters)
        m *= -1

    ans = str(s)
    t = str(target)

    #Print the results
    print('The combined volume of all ' + t + ' cuboids is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
target = 50000
solve(target)
