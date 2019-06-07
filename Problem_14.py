'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
Link: https://projecteuler.net/problem=14'''

#Imports
import time

#Chain length function
def chainlength(n):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        count += 1
    return count

#Solve function
def solve(n):
    start = time.time()
    longest = 0
    startingnum = 0

    for i in range(1, n):
        length = chainlength(i)
        if length > longest:
            longest = length
            startingnum = i

    print 'The starting number under ' + str(n) + ' with the longest chain is ' + str(startingnum) + '.'
    print 'The chain for ' + str(startingnum) + ' is ' + str(longest) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 1000000
solve(n)
