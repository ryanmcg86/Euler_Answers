'''This function returns the number of positive divisors of n'''
def pfExps(n):
	exps = []
	for i in range(2, 4):
		if n % i == 0:
			exps.append(0)
			while n % i == 0:
				n /= i
				exps[-1] += 1
	for i in range(5, int(n**0.5) + 1, 6):
		for j in [i, i + 2]:
			if n % j == 0:
				exps.append(0)
				while n % j == 0:
					n /= j
					exps[-1] += 1
	if n > 2:
		exps.append(1)
	return exps

def tau(n):
	exps = pfExps(n)
	ans = 1
	for i in exps:
		ans *= (i + 1)
	return ans
