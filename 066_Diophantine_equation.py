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
def solvePell(D):
    x = int(D**0.5)
	y, z, r = x, 1, x * 2
	n1, d1, n2, d2 = 0, 1, 1, 0
	while True:
		y = r * z - y
		z = (D - y**2) // z
		r = (x + y) // z
		d1, d2 = d2, d1 + d2 * r
		n1, n2 = n2, n1 + n2 * r
		a, b = n2 * x + d2, n2
		if a**2 - D * b**2 == 1:
			return [D, a, b]

#Build a solve function
def solve(num):
    #Define variables
    s = time.time()
    largesti, ansD, f = 0, 0, []
    
    #Solve the problem
    for i in range(num + 1):
        if i**0.5 == int(i**0.5):
            f.append([i, 0, 0])
            continue
        f.append(solvePell(i))
        result = f[len(f) - 1][1]
        if result > largesti:
            largesti = result
            ansD = i
            
    x, D, y = str(f[ansD][1]), str(f[ansD][0]), str(f[ansD][2])
    e = str(x + '^2 - ' + D + ' * ' + y + '^2 = 1')

    #Print the results
    print('When D ≤ ' + str(num) + ' in minimal solutions of x, the ')
    print('largest value of x is obtained when D = ' + str(ansD) + '.')
    print('In this case: ')
    print('x = ' + x + ', ')
    print('y = ' + y + ', ')
    print('and the quadratic Diophantine equation is: ')
    print(e)
    print('This took ' + str(time.time() - s) + ' seconds to calculate.')

#Run the program
num = 100
solve(num)
