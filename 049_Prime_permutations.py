'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
Link: https://projecteuler.net/problem=49'''

#Imports
import time

#Build a SoE function
def SoE(n):
    prime = [False] * 2 + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
    return [i for i in range(n) if prime[i]]

#Build a solve function
def solve():
    #Declare variables
    s = time.time()
    diff, diff2, maximum = 3330, 6660, 10**4
    soe, ans = SoE(maximum), ''
    search = {i: i for i in soe}
    begin, end, i = 1000, maximum - diff2, 1
    
    #Solve the problem
    while soe[i] < end:
        while soe[i] < begin: 
            i += 1   
        x, y, z = soe[i], soe[i] + diff, soe[i] + diff2
        if y in search:
            if z in search:
                a, b, c = str(x), str(y), str(z)
                sa, sb, sc = sorted(a), sorted(b), sorted(c)
                if sa == sb == sc and x != 1487:
                    ans = a + b + c
                    i = len(soe) - 2
        i += 1

    #Print the results
    print('The 12-digit number formed by concatenating ')
    print('the three terms in this sequence is ' + ans + '.')
    print('This took ' + str(time.time() - s) + ' seconds to calculate.')

#Run the program
solve()
