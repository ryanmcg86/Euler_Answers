'''In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of 
the numbers it contains is the smallest possible.

In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.

             15
         -14   -7
       20   -13  -5
     -3    8   23  -26
   1   -4    -5  -18   5
-16  31    2    9   28   3

We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers 
sk in the range ±219, using a type of random number generator (known as a Linear Congruential Generator) as follows:

t := 0 
for k = 1 up to k = 500500: 
    t := (615949*t + 797807) modulo 220
    sk := t−219

Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:

s1
s2  s3
s4  s5  s6  
s7  s8  s9  s10
...
Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements 
directly below it from the next row, the three elements directly below from the row after that, and so on). 
The "sum of a sub-triangle" is defined as the sum of all the elements it contains. 
Find the smallest possible sub-triangle sum.
Link: https://projecteuler.net/problem=150'''

#Imports
import time

#Build a Linear Congruential Generator function
def LCG(size):
    t = 0
    for k in range(size * (size + 1) / 2):
        t = (615949 * t + 797807) % 1048576  #1048576 = 2**20
        yield t - 524288                     # 524288 = 2**19

#Build a Solve function
def solve(size):
    #Define variables
    start = time.time()
    lcg = LCG(size)
    triangle = []
    minimum = 9999999999
    for rowcount in range(1, size + 1):
        row = []
        for i in range(rowcount):
            row.append(lcg.next())
        triangle.append(row)
    
    #Solve the problem
    for top_row in range(10):
        oldmin = minimum
        for top_col in range(len(triangle[top_row])):
            temp_min = 0
            right_col = top_col
            for row in range(top_row, size):
                right_col += 1
                temp_min  += sum(triangle[row][top_col:right_col])
                minimum    = min(temp_min, minimum)
                
    ans = str(minimum)
    size = str(size)
    
    #Print the results
    print 'The smallest possible sub-triangle sum in a '
    print size + '-row triangle generated with a Linear '
    print 'Congruential Generator is ' + ans + '.'   
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
size = 1000
solve(size)
