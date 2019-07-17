'''NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing 
in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; 
the sum is equal to 994.

                                    131 673 234 103  18
                                    201  96 342 965 150
                                    630 803 746 422 111
                                    537 699 497 121 956
                                    805 732 524  37 331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, from the left 
column to the right column.
Link: https://projecteuler.net/project/resources/p082_matrix.txt
Link: https://projecteuler.net/problem=82'''

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
    minimums = [0 for i in range(0, size)]
    
    for i in range(size - 2, -1, -1):
        for j in range(0, size):
            total = matrix[j][i]
            minimums[j] = total + matrix[j][i + 1]
            
            for k in range(j + 1, size):
                total += matrix[k][i]
                minimums[j] = min(minimums[j], total + matrix[k][i + 1])
                
            total = matrix[j][i]
            
            for k in range(j - 1, -1, -1):
                total += matrix[k][i]
                minimums[j] = min(minimums[j], total + matrix[k][i + 1])
                
        for j in range(0, size):
            matrix[j][i] = minimums[j]
            
    ans = str(min(minimums))
    
    #Print the results
    print 'The minimal path sum, in ' + name + ', from the left column to '
    print 'the right column by only moving right, up, or down, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
name = 'matrix.txt'
solve(name)
