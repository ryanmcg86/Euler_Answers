'''Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D = 13, the minimal solution in x is 649^2 – 13 × 180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2 × 2^2 = 1
2^2 – 3 × 1^2 = 1
9^2 – 5 × 4^2 = 1
5^2 – 6 × 2^2 = 1
8^2 – 7 × 3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D = 5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
Link: https://projecteuler.net/problem=66'''

#Imports
import time

#Build a fundamental solution function
def minX(D):
    n1, d1, n2, d2 = 0, 1, 1, 0
    found = False
    while not found:
        a = n1 + n2
        b = d1 + d2
        t = a**2 - D * b**2
        if t == 1:
            ansA = a
            found = True
        elif t == 0:
            print 'error'
            break
        else:
            if t < 0:
                n2 = a
                d2 = b
            else:
                n1 = a
                n2 = b
    return ansA

#Build a solve function
def solve(num):
    #Define variables
    start    = time.time()
    largesti = 0
    ansD = 0
    
    #Solve the problem
    for i in range(2, num + 1):
        if i**0.5 == int(i**0.5):
            continue
        result = minX(i)
        if result > largesti:
            largesti = result
            ansD = i

    #Print the results
    print 'The value of D ≤ ' + str(num) + ' in minimal solutions of x for '
    print 'which the largest value of x is obtained is ' + str(ansD) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 100
solve(num)
