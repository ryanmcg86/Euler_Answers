'''A k-input binary truth table is a map from k input bits (binary digits, 0 [false] or 1 [true]) to 1 output bit. 
For example, the 2-input binary truth tables for the logical AND and XOR functions are:

x   y   x AND y
0   0   0
0   1   0
1   0   0
1   1   1

x   y   x XOR y
0   0   0
0   1   1
1   0   1
1   1   0

How many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

for all 6-bit inputs (a, b, c, d, e, f)?
Link: https://projecteuler.net/problem=209'''

#Imports
import time
import math

#Build a number to binary function
def numToBin(n):
    s = bin(n)[2:]
    while len(s) < 6: s = '0' + s
    return [int(i) for i in s[::-1]]

#Build a binary to number function
def binToNum(bb):
    factor = 1
    tot = 0
    for i in bb:
        if i == 1: tot += factor
        factor *= 2
    return tot

#Build a switch function
def switch(n):
    a, b, c, d, e, f = numToBin(n)
    return binToNum([b, c, d, e, f, a^(b & c)])

#Build a build-a-set function
def buildSet(graphs):
    result = []
    count = 0
    used = set()
    t = [i for i in range(64)]
    for i in graphs:
        used.add(i[0])
        chain = [i[0]]
        n = i[1]
        if i[0] == i[1]:
            result.append(len(chain))
            t.remove(n)
            continue
        else:
            if i[0] in t: t.remove(i[0])
        if n in t:
            while n not in used:
                t.remove(n)
                used.add(n)
                n = graphs[n][1]
                chain.append(n)
            result.append(len(chain))
    return result

#Build a lucas function
def lucas(n):
    a, b = 2, 1
    if n == 0: return a
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b

#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    graphs = [[n, switch(n)] for n in range(64)]

    #Solve the problem
    ans = str(math.prod(lucas(i) for i in buildSet(graphs)))

    #Print the results
    print('There are ' + ans + ' 6-input binary truth tables, ')
    print('t, that satisfy the formula: t(a, b, c, d, e, f) ')
    print('AND t(b, c, d, e, f, a XOR (b AND c)) for all 6-bit')
    print('inputs (a, b, c, d, e, f).')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
solve()
