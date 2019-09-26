'''Consider the set Ir of points (x,y) with integer co-ordinates in the interior of the circle with radius r, 
centered at the origin, i.e. x2 + y2 < r2.

For a radius of 2, I2 contains the nine points (0,0), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1). 
There are eight triangles having all three vertices in I2 which contain the origin in the interior. 

For a radius of 3, there are 360 triangles containing the origin in the interior and having all vertices in I3 
and for I5 the number is 10600.

How many triangles are there containing the origin in the interior and having all three vertices in I105?
Link: https://projecteuler.net/problem=184'''

#Imports
import time

#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    cache  = {}          #slopes_dictionary
    nbot   = 0           #number_of_triangles
    nbocb  = 0           #number_of_couples_below
    lnbocb = 0           #l_number_of_couples_below
    nbop   = 0           #number_of_points

    #Solve the problem
    for i in range(n + 1):
        for j in range(n + 1):
            if i**2 + j**2 < n**2:
                nbop += 1
                if i != 0 and j != 0:
                    s = float(j) / i
                    if s in cache: cache[s] += 1
                    else:          cache[s]  = 1

    slopes = cache.keys()
    sorted(slopes)
    nbopa = nbop - n     #number_of_points_above
	
    for s in slopes:
        nbopa -= cache[s]
        nbocb += (nbop - nbopa - cache[s] - n) * cache[s]    
        nbot += cache[s] * ((nbop - 1) * nbopa - (n - 1)**2 + lnbocb)
        lnbocb = nbocb

    ans = str(nbot * 4)
    n = str(n)

    #Print the results
    print('There are ' + ans + ' triangles containing the origin ')
    print('in the interior and having all three vertices in I(' + n + ').')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 105
solve(n)
