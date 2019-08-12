'''The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.

If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, 
the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen 
cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first 
layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, 
C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
Link: https://projecteuler.net/problem=126'''

#Imports
import time

#Build a number-of-cubes function
def numCubes(l, w, h, n):
    a = 2 * (l * w + l * h + w * h)
    b = 4 * n * (l + h + w)
    c = 4 * n * (n - 1)
    return a + b + c

#Build a Solve function
def Solve(n):
    #Define variables
    start = time.time()
    limit = n * 20
    check = [0] * limit
    i = 1
    ans = 0
    
    #Solve the problem
    while numCubes(i, i, i, 0) < limit:
        j = i
        while numCubes(i, j, j, 0) < limit:
            k = j
            while numCubes(i, j, k, 0) < limit:
                L = 0
                while numCubes(i, j, k, L) < limit:
                    check[numCubes(i, j, k, L)] += 1
                    L += 1
                k += 1
            j += 1
        i += 1
    
    for i in range(0, limit):
        if check[i] == n:
            ans = str(i)
            break
            
    n = str(n)

    #Print the results
    print 'The least value of n for which C(n) = ' + n + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 1000
Solve(n)
