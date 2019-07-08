'''The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly 
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
Link: https://projecteuler.net/problem=62'''

#Imports
import time

#Build an isCube function
def isCube(n):
    base = int(n**(1/3.0))
    return base**3 == n or (base + 1)**3 == n

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    begin = 345
    limit = 5
    cubes = dict()
    found = False
    ans = 0
    n = begin

    #Solve the problem
    while not found:
        cube = n**3
        k = ''.join(sorted(str(cube)))
        if k not in cubes:
            cubes[k] = set()
        cubes[k].add(cube)
        if len(cubes[k]) == limit:
            found = True
            ans = str(min(cubes[k]))
        n += 1

    #Print the results
    print 'The smallest cube for which exactly five permutations '
    print 'of its digits are also cubes is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
