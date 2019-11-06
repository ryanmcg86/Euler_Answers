'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
Link: https://projecteuler.net/problem=32'''

#Imports
import time

#Build a sum-of-products function
def sumOfProds(n):
    #Declare variables
    start = time.time()
    panprods = set()
    nums = '123456789'
	
    #Solve the problem
    for i in range(2, 80):
        for j in range(2, 10000 // i):
            num = str(i) + str(j) + str(i * j)
            if len(num) == n and not nums[:n].strip(num):
			panprods.add(i * j)
    ans = str(sum(panprods))

    #Print the results
    print('The sum of all products whose multiplicand/')
    print('multiplier/product identity can be written ')
    print('as a 1 though ' + n + ' pandigital is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program			
n = 9
sumOfProds(n)
