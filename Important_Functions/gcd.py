'''This function returns the greatest common divisor (gcd, or, 
the Highest Common Factor) for two given inputs'''

def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
