'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
Link: https://projecteuler.net/problem=32'''

#Imports
from itertools import permutations
import time

#Build a sum-of-products function
def sumOfProds(digits):
	start = time.time()

	total = []
	baseperm = []
	for i in range(1, digits + 1):
		baseperm.append(i)
	perm = permutations(baseperm)
	perms = []
	for i in list(perm):
		perms.append(i)

	for i in range(0, len(perms)):
		perm = ''
		for j in range(0, len(perms[i])):
			perm += str(perms[i][j])
		for j in range(2, len(perms[i])):
			for k in range(1, j):
				num1 = int(perm[0:k])
				num2 = int(perm[k:j])
				num3 = int(perm[j:digits])
				a = len(str(num1))
				b = len(str(num2))
				c = len(str(num3))
				if a > c or b > c:
					break
				if num1 * num2 == num3:
					total.append(num3)
	total = set(total)
	ans = str(sum(total))

	print 'The sum of all products whose multiplicand/multiplier/product'
	print 'identity can be written as a 1 though ' + str(digits)
	print 'pandigital is ' + ans + '.'
	print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program			
digits = 9
sumOfProds(digits)
