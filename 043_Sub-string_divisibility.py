'''The number, 1406357289, is a 0 to 9 pandigital number because it is made 
up of each of the digits 0 to 9 in some order, but it also has a rather 
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4  = 406 is divisible by 2
d3d4d5  = 063 is divisible by 3
d4d5d6  = 635 is divisible by 5
d5d6d7  = 357 is divisible by 7
d6d7d8  = 572 is divisible by 11
d7d8d9  = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
Link: https://projecteuler.net/problem=43'''

#Imports
import time

#Build a solve function
def solve():
	start       = time.time()
	total       = 0
	digits      = {str(i) for i in range(0, 10)}
	primes      = [13, 11, 7, 5, 3, 2, 1]
	pandigitals = []
    
    #Start with the 3 digit numbers divisible by 17,
    #GREATLY reducing the numbers we need to check
	for i in range(102, 983, 17):
		num = str(i)
        #if the number has 3 unique digits, add it to the list
		if len(set(num)) == len(num):
			pandigitals.append(num)
     
	for p in primes:
		temp = []
		for n in pandigitals:
			nums = list(digits - set(n))
            #Add each of the remaining digits not in 
            #n to the front of n, and see if it's
            #divisible by p. If it is, add it to temp
			for num in nums:
				testnum = num + n
				if int(testnum[0:3]) % p == 0:
					temp.append(str(t))
        #Replace the current pandigitals with the updated
        #possible numbers
		pandigitals = temp
    
    #Sum up all the pandigitals found that have the given property
	total = str(sum(list(map(int, pandigitals))))

    #Print the results
	print 'The sum of all 0 to 9 pandigital numbers with the given'
	print 'property is ' + total + '.'
	print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
