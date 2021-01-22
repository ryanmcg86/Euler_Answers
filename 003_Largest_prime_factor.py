'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
Link: https://projecteuler.net/problem=3'''

#Imports
import time

#Build a factors function
def factors(num):
	if num == 2: return [num]
	factors, p = [], 2
	while p**2 <= num:
		if num % p == 0:
			factors.append(p)
			num //= p
		else:
			if p > 3 and (p + 1) % 6 != 0: p += 4
			elif p > 2: p += 2
			else: p += 1
	if num > 2: factors.append(num)
	return factors

#Largest prime factor function
def lpf(n):
    #Declare variables
    start = time.time()
    
    #Solve the problem
    ans = str(factors(n)[-1])
    n = str(n)
    
    #Print the results
    print 'The largest prime factor of ' + n + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 600851475143
lpf(n)
