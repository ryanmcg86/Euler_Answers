'''A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. 
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest 
route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, 
up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. 
This is the least value of M for which the number of solutions first exceeds two thousand; 
the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
Link: https://projecteuler.net/problem=86'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    count = 0
    M = 2

    #Solve the problem
    while count <= limit:
        M += 1
        c = M
        for ab in range(2, 2 * M + 1):
            if ((ab**2 + c**2)**0.5) % 1 == 0:
                if ab >= c:
                    count += c - int((ab + 1) / 2) + 1
                else:
                    count += int(ab / 2)
                    
    ans = str(M)

    #Print the results
    print 'The least value of M such that the number '
    print 'of solutions first exceeds ' + str(limit) + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 10**6
solve(limit)
