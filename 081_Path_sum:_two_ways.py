'''In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, 
is equal to 2427.

                               131 673 234 103  18 
                               201  96 342 965 150 
                               630 803 746 422 111 
                               537 699 497 121 956 
                               805 732 524  37 331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, 
from the top left to the bottom right by only moving right and down.
https://projecteuler.net/project/resources/p081_matrix.txt
Link: https://projecteuler.net/problem=81'''

#Imports
import time

#Build a solve function
def solve(name):
    #Define variables
    start = time.time()
    
    #Solve the problem
    with open(name, 'r') as f:
        matrix = [[int(v) for v in line.split(',')] for line in f]
        
    size = len(matrix)
    
    for i in range(size - 2, -1, -1):
        matrix[i][-1] += matrix[i + 1][-1]
        matrix[-1][i] += matrix[-1][i + 1]
        
    for i in range(size - 2, -1, -1):
        for j in range(size - 2, -1, -1):
            matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])
            
    ans = str(matrix[0][0])
    
    #Print the results
    print 'The minimal path sum, in ' + name + ' , from the top left to '
    print 'the bottom right by only moving right and down, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
name = 'matrix.txt'
solve(name)
