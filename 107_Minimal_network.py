'''An undirected network consists of seven vertices and twelve edges with a total weight of 243.

The same network can be represented by the matrix below.
        A  B  C  D  E  F  G
     A  -- 16 12 21 -- -- --
     B  16 -- -- 17 20 -- --
     C  12 -- -- 28 -- 31 --
     D  21 17 28 -- 18 19 23
     E  -- 20 -- 18 -- -- 11
     F  -- -- 31 19 -- -- 27
     G  -- -- -- 23 11 27 --
However, it is possible to optimise the network by removing some edges and still ensure that 
all points on the network remain connected. The network which achieves the maximum saving  has a weight of 93, 
representing a saving of 243 − 93 = 150 from the original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, 
and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring 
that the network remains connected.
Link: https://projecteuler.net/project/resources/p107_network.txt
Link: https://projecteuler.net/problem=107'''

#Imports
import time

#Build a solve function
def solve(filename):
    #Define variables
    start = time.time()
    edges = set()
    
    #Solve the problem
    for v1, line in enumerate(open(filename)):
        for v2, weight in enumerate(line.split(',')):
            if weight.strip() != '-':
                i, j = v1 > v2 and (v1, v2) or (v2, v1)
                edges.add((int(weight), i, j))
                
    tot = sum(w for (w, v1, v2) in edges)
    groups = dict((i, i) for i in range(len(edges)))
    newtot = 0
    
    for w, v1, v2 in sorted(edges):
        if groups[v1] != groups[v2]:
            for vert in [v for (v, g) in groups.items() if g == groups[v2]]:
                groups[vert] = groups[v1]
            newtot += w
            if len(set(groups.values())) == 1:
                break
                
    ans = str(tot - newtot)
    
    #Print the results
    print 'Using ' + filename + ', the maximum saving which can '
    print 'be achieved by removing redundant edges whilst '
    print 'ensuring that the network remained connected is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'network.txt'
solve(filename)
