'''A triomino is a shape consisting of three squares joined via the edges. There are two basic forms:

                             **                   ***
                             *

If all possible orientations are taken into account there are six:

                         **     **     *       *     *       ***
                         *       *     **     **     *
                                                     *

Any n by m grid for which n x m is divisible by 3 can be tiled with triominoes.
If we consider tilings that can be obtained by reflection or rotation from another tiling as different there are 
41 ways a 2 by 9 grid can be tiled with triominoes

In how many ways can a 9 by 12 grid be tiled in this way by triominoes?
Link: https://projecteuler.net/problem=161'''

#Imports
import time

#Build a numTilings function
def numTilings(squares, tileDict):
    if len(squares) == 0: return 1
    
    squareTuple = tuple(sorted(squares))
    if squareTuple in tileDict:
        return tileDict[squareTuple]

    corner = min(squares)
    x = corner[0]
    y = corner[1]

    #The 6 possible orientations, named to look as much like
    #their shape as possible
    L = {(0,  1), (1, 1)} # L
    J = {(1, -1), (1, 0)} # J
    r = {(0,  1), (1, 0)} # r
    s = {(1,  0), (1, 1)} # 7, s for seven
    I = {(0,  1), (0, 2)} # |
    h = {(1,  0), (2, 0)} # -, h for hyphen, or horizontal
    trominoes = [L, J, r, s, I, h]

    n = 0

    for t in trominoes:
        otherSquares = {(x + sq[0], y + sq[1]) for sq in t}
        if otherSquares & squares == otherSquares:
            n += numTilings(squares - {corner} - otherSquares, tileDict)

    tileDict[squareTuple] = n
    return n
   
#Build a Solve function
def solve(w, h):
    #Define variables
    start = time.time()
    tileDict = {}
    if h > w:
        w, h = h, w
    grid = {(a, b) for a in range(w) for b in range(h)}
    
    #Solve the problem
    ans = str(numTilings(grid, tileDict))
    
    grid = str(h) + 'x' + str(w)
        
    #Print the results
    print 'A ' + grid + ' grid can be tiled  by triominoes '
    print 'in ' + ans + ' different ways.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
w, h = 12, 9
solve(w, h)
