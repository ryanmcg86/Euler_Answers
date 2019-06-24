'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may 
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
Link: https://projecteuler.net/problem=33'''

#Imports
from fractions import Fraction
import time

#Build a Solve function
def Solve():
    start = time.time()

    fractions = []

    for i in range(10, 100):
        for j in range(10, 100):
            fdnum = str(i)[0]
            sdnum = str(i)[1]
            fdden = str(j)[0]
            sdden = str(j)[1]
            if sdden == '0':
                continue
            small = int(fdnum) / float(sdden)
            orig = i / float(j)
            if sdnum == fdden:
                if small == orig and i != j:
                    fractions.append([i, j])

    num = 1
    den = 1
    for i in range(0, len(fractions)):
        num *= fractions[i][0]
        den *= fractions[i][1]

    ans = str(Fraction(num, den))[str(Fraction(num, den)).find('/') + 1:]

    print 'The value of the denominator of the product of '
    print 'the 4 2-digit-cancelling fractions is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program			
Solve()
