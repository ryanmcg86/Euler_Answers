'''If we are presented with the first k terms of a sequence it is impossible to say with 
certainty the value of the next term, as there are infinitely many polynomial functions that can model the sequence.

As an example, let us consider the sequence of cube numbers. This is defined by the generating function, 
un = n3: 1, 8, 27, 64, 125, 216, ...

Suppose we were only given the first two terms of this sequence. Working on the principle that 
"simple is best" we should assume a linear relationship and predict the next term to be 15 (common difference 7). 
Even if we were presented with the first three terms, by the same principle of simplicity, a quadratic 
relationship should be assumed.

We shall define OP(k, n) to be the nth term of the optimum polynomial generating function for the first 
k terms of a sequence. It should be clear that OP(k, n) will accurately generate the terms of the sequence 
for n ≤ k, and potentially the first incorrect term (FIT) will be OP(k, k+1); in which case we shall call it a bad OP (BOP).

As a basis, if we were only given the first term of sequence, it would be most sensible to assume constancy; 
that is, for n ≥ 2, OP(1, n) = u1.

Hence we obtain the following OPs for the cubic sequence:

OP(1, n) = 1                    1, 1, 1, 1, ...
OP(2, n) = 7n−6	                1, 8, 15, ...
OP(3, n) = 6n^2 − 11n + 6     	1, 8, 27, 58, ...
OP(4, n) = n^3	                1, 8, 27, 64, 125, ...
Clearly no BOPs exist for k ≥ 4.

By considering the sum of FITs generated by the BOPs (indicated in red above), we obtain 1 + 15 + 58 = 74.

Consider the following tenth degree polynomial generating function:

un = 1 − n + n^2 − n^3 + n^4 − n^5 + n^6 − n^7 + n^8 − n^9 + n^10

Find the sum of FITs for the BOPs.
Link: https://projecteuler.net/problem=101'''

#Imports
import time

#Build a buildSuffix function
def buildSuffix(num):
    suffs = ['th', 'st', 'nd', 'rd']
    suff = suffs[0]
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        lastdigit = int(str(num)[-1])
        if lastdigit < len(suffs):
            suff = suffs[lastdigit]
    return suff

#Build a findnext function
def findnext(x):
    l = len(x)
    if l == 1:
        return x[0]
    return x[-1] + findnext([x[i + 1] - x[i] for i in range(l - 1)])

#Build a u function
def u(n):
    return sum([(-n)**i for i in range(11)])

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    total = 0
    U = [u(i + 1) for i in range(11)]
    
    #Solve the problem
    for n in range(1, limit + 1):
        fit = findnext(U[:n])
        if fit != U[n]:
            total += fit
            
    ans = str(total)
    lim = str(limit) + buildSuffix(limit)
    #Print the results
    print 'The sum of FITs for the BOPs for a ' + lim + ' degree polynomial is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10
solve(limit)