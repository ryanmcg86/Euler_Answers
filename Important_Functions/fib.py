'''This is a O(log n) implementation of a function that retreives the nth number in Fibonacci's sequence.'''

fibs = {0: 0, 1: 1}

def fib(n):
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
    else:
        fibs[n] = fib((n - 1) / 2)**2 + fib((n + 1) / 2)**2
    return fibs[n]
