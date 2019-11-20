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
def solve9():
	#Define variables
	start       = time.time()
	digits      = {str(i) for i in range(10)}
	primes      = [13, 11, 7, 5, 3, 2, 1]  #Include 1 with the primes, as we have to add a leading digit 7 total times.
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
		for valids in pandigitals:
			nums = list(digits - set(valids))
			#Add each of the remaining digits not in 
			#nums to the front of nums, and see if it's
			#divisible by p. If it is, add it to temp
			for num in nums:
				new = num + valids
				if int(new[:3]) % p == 0:
					temp.append(str(new))
		#Replace the current pandigitals with
		#the updated possible numbers
		pandigitals = temp

	#Sum up all the pandigitals found that have the given property
	total = str(sum(list(map(int, pandigitals))))

	#Print the results
	print 'The sum of all 0 to 9 pandigital numbers with the given'
	print 'property is ' + total + '.'
	print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve9()
#----------------------------------Hackerrank Version----------------------------------#
#Imports
import time

#Define a next_permutation function
def next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i + 1]): i -= 1
    if i < 0: return False
    j = len(a) - 1
    while not (a[j] > a[i]): j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

#Define a main function
def main(n = 9):
    #Define variables
    v = [i for i in range(n + 1)]
    s = 0
    p = [2, 3, 5, 7, 11, 13, 17]
	
    #Solve the problem
    if n == 9: return solve9()
    while True:
        sat = True
        num = 10 * v[1] + v[2]
        for ind in range(3, n + 1):
            num = num % 100
            num = num * 10 + v[ind]
            if num % p[ind - 3] != 0:
                sat = False
                break
        if sat:
            s += int(''.join(str(i) for i in v))
        if next_permutation(v) == False: break
		
    #Return the result
    return s

print(main(int(input())))

#Don't run this in Hackerrank, but to formalize the answer and time it:
def solve(n):
    start = time.time()
    ans, n = str(main(n)), str(n)
    print('The sum of all 0 to ' + n + ' pandigital numbers ')
    print('with the given property is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Print all the results
for i in range(3, 10):
    print('')
    solve(i)
