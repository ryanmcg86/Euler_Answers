'''The square root of 2 can be written as an infinite continued fraction.

√2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + ...))))
The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. 
In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. 
Let us consider the convergents for √2.

1 + (1 / 2) = 3 / 2
1 + (1 / (2 + (1 / 2))) = 7 / 5
1 + (1 / (2 + (1 / (2 + (1 / 2))))) = 17 / 12
1 + (1 / (2 + (1 / (2 + (1 / (2 + (1 / 2))))))) = 41 / 29
Hence the sequence of the first ten convergents for √2 are:

1, 3 / 2, 7 / 5, 17 / 12, 41 / 29, 99 / 70, 239 / 169, 577 / 408, 1393 / 985, 3363 / 2378, ...
What is most surprising is that the important mathematical constant,
e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].

The first ten terms in the sequence of convergents for e are:

2,3, 8 / 3, 11 / 4, 19 / 7, 87 / 32, 106 / 39, 193 / 71, 1264 / 465, 1457 / 536, ...
The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
Link: https://projecteuler.net/problem=65'''

#Imports
import time

#Build a suffix function
def buildSuffix(num):
    suff = 'th'
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        if   int(str(num)[-1]) == 1:
            suff = 'st'
        elif int(str(num)[-1]) == 2:
            suff = 'nd'
        elif int(str(num)[-1]) == 3:
            suff = 'rd'
    return suff

#Build a solve function
def solve(num):
    #Define variables
    start    = time.time()
    n0 = 2
    n1 = 3
    k  = 2
    ans = ''
    suff = ''
    warn = 'You need to enter a number larger than 0. '
    if num < 1:
        return warn + 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
    #Solve the problem
    for i in range(3, num + 1):
        if i % 3 == 0:
            tempn1 = n1
            n1 = n1 * k + n0
            n0 = tempn1
            k += 2
        else:
            tempn1 = n1
            n1 = n1 + n0
            n0 = tempn1
    
    if num == 1:
        ans = str(2)
    else:
        ans = str(sum(int(i) for i in str(n1)))
    num = str(num) + buildSuffix(num)

    #Print the results
    print 'The sum of digits in the numerator of the ' + num
    print 'convergent of the continued fraction for e is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 100
solve(num)
