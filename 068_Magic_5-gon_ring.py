'''Consider the "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), 
each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
What is the maximum 16-digit string for a "magic" 5-gon ring?
Link: https://projecteuler.net/problem=68'''

#Imports
import itertools as t
import time

#Define a function that determines if the input is a 
#proper gon ring.
def itsagon(gon):
    sum1 = gon[0] + gon[1] + gon[2]
    sum2 = gon[3] + gon[2] + gon[4]
    sum3 = gon[5] + gon[4] + gon[6]
    sum4 = gon[7] + gon[6] + gon[8]
    sum5 = gon[9] + gon[8] + gon[1]
    return sum1 == sum2 == sum3 == sum4 == sum5

#Build a run function
def run():
    #Declare variables
    start = time.time()
    gon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    perms = list(t.permutations(gon))
    relevantperms = []
    largestNum = 1
    
    #Solve
    for i in perms:
        if itsagon(i) and i[0] < i[3] and i[0] < i[5] and i[0] < i[7] and i[0] < i[9]:
            relevantperms.append(i)
    
    for i in relevantperms:
        result = ''
        result += str(i[0]) + str(i[1]) + str(i[2])
        result += str(i[3]) + str(i[2]) + str(i[4])
        result += str(i[5]) + str(i[4]) + str(i[6])
        result += str(i[7]) + str(i[6]) + str(i[8])
        result += str(i[9]) + str(i[8]) + str(i[1])
        if largestNum < int(result) and len(result) < 17:
            largestNum = int(result)

    #print results
    print 'The maximum 16-digit string for a "magic" 5-gon ring is ' + str(largestNum) + '.'
    print 'It took ' + (time.time() - start) + ' seconds to find the result.'
    
#Run the program
run()
