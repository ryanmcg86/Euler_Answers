'''By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.


Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.
Link: https://projecteuler.net/problem=85'''

#Imports
import time

#Build an amount function
'''
I initially came up with the following function:

def amount(x, y):
    return sum((x - i) * (y - j) for i in range(x) for j in range(y))
    
but after some research found that this is MUCH faster:
''''
def amount(x, y):
    return int(0.25 * (x**2 + x) * (y**2 + y))

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    i = 1
    j = 1
    I = 0
    J = 0
    closest = 999999
    num = amount(i, j)

    #Solve the problem
    while num <= limit:
        while num <= limit:
            diff = abs(limit - num)
            if diff < closest:
                closest = diff
                I = i
                J = j
            i += 1
            num = amount(i, j)
        j += 1
        i = 1
        num = amount(i, j)

    ans = str(I * J)

    #Print the results
    print 'The area of the grid closest to ' + str(limit) + ' squares is ' + ans + '.'
    print 'The ' + str(I) + ' by ' + str(J) + ' grid in question has ' + str(amount(I, J)) + ' squares.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 2 * 10**6
solve(limit)
