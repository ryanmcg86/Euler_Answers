'''This function returns the lowest common multiple for two given inputs'''

def lcm(a, b):
    a1 = a
    b1 = b
    while b != 0:
        i = a
        a = b
        b = i % b
    return a1 * b1 // a
