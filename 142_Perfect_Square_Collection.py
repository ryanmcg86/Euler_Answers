'''Find the smallest x + y + z with integers x > y > z > 0 such that x + y, 
x − y, x + z, x − z, y + z, y − z are all perfect squares.
Link: https://projecteuler.net/problem=142'''

#Imports
import time
    
#Build an isSquare function
def isSquare(n):
    return n**0.5 == int(n**0.5)
    
#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    ans = 0
    found = False
    x = 1
    X, Y, Z = 0, 0, 0
    
    #Solve the problem
    while not found:
        x1 = x**2
        if found: break
        for y in range(x % 2, x, 2):
            if y == 0: continue
            y1 = y**2
            if isSquare(x1 - y1):
                if found: break
                for z in range(x % 2, y, 2):
                    if z == 0: continue
                    z1 = z**2
                    if isSquare(y1 - z1) and isSquare(x1 + z1 - y1):
                        X = ((x1 + z1) / 2)
                        Y = ((x1 - z1) / 2)
                        Z = ((x1 + z1) / 2 - y1)
                        ans = str(X + Y + Z)
                        found = True
                        break
        x += 1
    
    xyz = ', where x = ' + str(X) + ', y = ' + str(Y) + ', and z = ' + str(Z)
    
    #Print the results
    print 'The smallest x + y + z with integers x > y > z > 0 such that '
    print 'x + y, x - y, x + z, x - z, y + z, and y - z are all perfect '
    print 'squares is ' + ans + xyz + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
solve()
