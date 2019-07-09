'''All square roots are periodic when written as continued fractions and can be written in the form:

√N = a0 + (1 / a1 + (1 / a2 + (1 / a3 + …)))

For example, let us consider √23:

√23 = 4 + √23 − 4 = 4 + 1 / (1 / (√23 − 4)) = 4+  1 / (1 + ((√23 − 3) / 7))

If we continue we would get the following expansion:

√23 = 4 + (1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + …)))))

The process can be summarised as follows:

a0 = 4, 1 / (√23 − 4) =      (√23 + 4)  /  7 = 1 + (√23 − 3 / 7)

a1 = 1, 7 / (√23 − 3) = (7 * (√23 + 3)) / 14 = 3 + (√23 − 3 / 2)

a2 = 3, 2 / (√23 − 3) = (2 * (√23 + 3)) / 14 = 1 + (√23 − 4 / 7)

a3 = 1, 7 / (√23 − 4) = (7 * (√23 + 4)) /  7 = 8 + √23 − 4

a4 = 8, 1 / (√23 − 4) =      (√23 + 4)  /  7 = 1 + (√23 − 3 / 7)

a5 = 1, 7 / (√23 − 3) = (7 * (√23 + 3)) / 14 = 3 + (√23 − 3 / 2)

a6 = 3, 2 / (√23 − 3) = (2 * (√23 + 3)) / 14 = 1 + (√23 − 4 / 7)

a7 = 1, 7 / (√23 − 4) = (7 * (√23 + 4)) /  7 = 8 + √23 − 4



It can be seen that the sequence is repeating. For conciseness, we use the notation 
√23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2 = [1;(2)], period = 1

√3 = [1;(1,2)], period = 2

√5 = [2;(4)], period = 1

√6 = [2;(2,4)], period = 2

√7 = [2;(1,1,1,4)], period = 4

√8 = [2;(1,4)], period = 2

√10 = [3;(6)], period = 1

√11 = [3;(3,6)], period = 2

√12 = [3;(2,6)], period = 2

√13 = [3;(1,1,1,1,6)], period = 5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
Link: https://projecteuler.net/problem=64'''

#Imports
import time
import math

#Build a solve function
def solve(limit):
    #Define variables
    start    = time.time()
    oddCount = 0

    #Solve the problem
    for n in range(2, limit + 1):
        if n**0.5 % 1 == 0:        #if n is a square
            continue
        a = math.floor(n**0.5)
        b = math.floor(n**0.5)
        k = 1.0
        p_len = 0                  #period length
        while k != 1 or p_len == 0:
            k = (n - b * b) / k
            a = math.floor((n**0.5 + b) / k)
            b = a * k - b
            p_len += 1
        if p_len % 2 == 1:
            oddCount += 1

    #Print the results
    print 'For N <= ' + str(limit) + ', there are ' + str(oddCount)
    print 'continued fractions with an odd period.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10000
solve(limit)
