# Sieve of Eratosthenes implementation


def primes(n):
    ''' 
    Return a list of all primes upto n 
    e.g.    primes(10) == [2,3,5,7]
            primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''
    if n <= 2:
        return []

    sieve = [True] * (n + 1)
    for x in range(3, int(n**0.5) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2] + [i for i in range(3, n, 2) if sieve[i]]
