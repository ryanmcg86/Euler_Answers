'''A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size A5.

Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special paper with size A1.

He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them in half to get two sheets of size A3 
and so on until he obtains the A5-size sheet needed for the first batch of the week.

All the unused sheets are placed back in the envelope.

At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random. If it is of size A5, he uses it. 
If it is larger, he repeats the 'cut-in-half' procedure until he has what he needs and any remaining sheets are always placed back 
in the envelope.

Excluding the first and last batch of the week, find the expected number of times (during each week) that the foreman finds a single 
sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .
Link: https://projecteuler.net/problem=151'''

#Imports
import time

#Build a calculate function
def calc(a5, a4, a3, a2):
    res = 0.0
    left = 1.0 * (a5 + a4 + a3 + a2)
    if left == 1 and a5 != 1:
        res = 1.0
    if a5 > 0:
        res += a5 * calc(a5 - 1, a4, a3, a2)
    if a4 > 0:
        res += a4 * calc(a5 + 1, a4 - 1, a3, a2)
    if a3 > 0:
        res += a3 * calc(a5 + 1, a4 + 1, a3 - 1, a2)
    if a2 > 0:
        res += a2 * calc(a5 + 1, a4 + 1, a3 + 1, a2 - 1)
    if left > 0:
        res /= left
    return res

#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    
    #Solve the problem
    ans = str(round(calc(1, 1, 1, 1), 6))
    
    #Print the results
    print 'The expected number of times (during each week) that the foreman'
    print 'finds a single sheet of paper in the envelope is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
solve()
