'''This function tells whether the inputted number is pandigital or not'''

def isPan(n):
    num = ''.join(str(i) for i in range(1, len(str(n)) + 1))
    return num == ''.join(sorted(str(n)))
