'''It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
Link: https://projecteuler.net/problem=57'''

#Imports
import time

#Build a solve function
def solve(n):
    #Define variables
    start = time.time()
    a = 3
    b = 2
    count = 0

    #Solve the problem
    for i in range(0, n):
        if len(str(a)) > len(str(b)):
            count += 1
        tempA = a
        tempB = b
        a = (2 * tempB) + tempA
        b = tempA + tempB

    #Print the results
    print 'In the first ' + str(n) + ' expansions, there are ' + str(count) + ' fractions '
    print 'that contain a numerator longer than the denominator.' 
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 1000
solve(n)
