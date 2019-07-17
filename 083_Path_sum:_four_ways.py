'''NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, 
right, up, and down, is indicated in bold red and is equal to 2297.

                                        131 673 234 103  18
                                        201  96 342 965 150
                                        630 803 746 422 111
                                        537 699 497 121 956
                                        805 732 524  37 331

Find the minimal path sum, in matrix.txt , a 31K text file containing a 80 by 80 matrix, from the 
top left to the bottom right by moving left, right, up, and down.
Link: https://projecteuler.net/project/resources/p083_matrix.txt
Link: https://projecteuler.net/problem=83'''

#Imports
import time

#Build a solve function
def solve(name):
    #Define variables
    start = time.time()
    INFINITY = 1000000000
    
    #Solve the problem
    with open(name, 'r') as f:
        matrix = [[int(v) for v in line.split(',')] for line in f]
        
    size = len(matrix)
    visited = [[False for i in range(0, size)] for j in range(0, size)]
    distances = [[INFINITY for i in range(size)] for j in range(0, size)]
    distances[0][0] = matrix[0][0]
    queue = [(0, 0)]
    
    while len(queue) > 0:
        i, j = min(queue, key = lambda v: distances[v[0]][v[1]])
        queue.remove((i, j))
        visited[i][j] = True
        
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < size and 0 <= nj < size and not visited[ni][nj]:
                distances[ni][nj] = min(distances[ni][nj], distances[i][j] + matrix[ni][nj])
                
                if (ni, nj) not in queue:
                    queue.append((ni, nj))
            
    ans = str(distances[-1][-1])
    
    #Print the results
    print 'The minimal path sum, in ' + name + ', from the top left to '
    print 'the bottom right by moving left, right, up, or down, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
name = 'matrix.txt'
solve(name)
