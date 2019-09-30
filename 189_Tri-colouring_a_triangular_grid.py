'''Consider the following configuration of 64 triangles:

                                                    /\
                                                   /\/\
                                                  /\/\/\
                                                 /\/\/\/\
                                                /\/\/\/\/\
                                               /\/\/\/\/\/\
                                              /\/\/\/\/\/\/\
                                             /\/\/\/\/\/\/\/\


We wish to colour the interior of each triangle with one of three colours: red, green or blue, 
so that no two neighbouring triangles have the same colour. Such a colouring shall be called valid. 
Here, two triangles are said to be neighbouring if they share an edge.
Note: if they only share a vertex, then they are not neighbours.

A colouring C' which is obtained from a colouring C by rotation or reflection is considered distinct from 
C unless the two are identical.

How many distinct valid colourings are there for the above configuration?
Link: https://projecteuler.net/problem=189'''

#Imports
import time

#Build a nextRow function
def nextRow(pos, row, mem, odd, colors):
    if pos in mem: return mem[pos]
    if pos == len(row) + odd: return [()]
    mem[pos] = []
    for i in nextRow(pos + 1, row, mem, odd, colors):
        for j in range(colors):
            a = pos < len(row) and j == row[pos]
            b = pos and j == row[pos - 1]
            if odd and (a or b): continue
            elif (not odd) and j == row[pos]: continue
            mem[pos].append((j,) + i)
    return mem[pos]

#Build a Solve function
def solve(rows, colors):
    #Define variables
    start = time.time()
    row = {(0,): 1}

    #Solve the problem
    for i in range(rows - 1):
        for odd in range(2):
            row, lastRow = {}, row
            for j, k in lastRow.iteritems():
                for l in nextRow(0, j, {}, odd, colors):
                    row[l] = row.get(l, 0) + k
                    
    ans = str(colors * sum(row.itervalues()))
    col = str(colors)
    row = str(rows)

    #Print the results
    print('There are ' + ans + ' distinct valid colourings ')
    print('for a triangle with ' + row + ' rows and ' + col + ' colors.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
rows = 8
colors = 3
solve(rows, colors)
