#This code will give you the greatest common denominator amongst an array of numbers

def gen_gcd(nums):
    from functools import reduce
    def gcd(x, y):
        while y != 0:
            a = x
            x = y
            y = a % x
        return x
    return reduce(lambda x, y: gcd(x, y), nums)
    
'''
If you create an array of numbers, like this:

>>> nums = [20, 30, 60]

and then run the function, with the array as it's input:

>>> gen_gcd(nums)

it will output the greatest common denominator of 20, 30, and 60

>>> 10
'''
