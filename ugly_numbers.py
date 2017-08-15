def prime_factors(n):
    ''' 
    Get Prime Factors for a given number
    e.g.    prime_factors(18) == [2,3,3]
            prime_factors(60) == [2,2,3,5]
    '''

    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return factors


def is_ugly(n, ugly_list=[2, 3, 5]):
    '''
    Ugly numbers are positive numbers whose prime factors only include prime numbers from the ugly_list
    Returns True if given number (n) is ugly, else False
    '''
    prime_factors_of_n = set(prime_factors(n))
    ugly_set = set(ugly_list)
    if prime_factors_of_n.difference(ugly_set):
        return False
    return True


def ugly_generator(n):
    ''' Generates the first 'n' ugly numbers '''
    yield 1
    n -= 1
    i = 2
    while n:
        if is_ugly(i):
            yield i
            n -= 1
        i += 1


def main():
    # Print first 10 ugly numbers
    assert list(ugly_generator(10)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

    # Print 23rd ugly number
    assert list(ugly_generator(23))[-1] == 48


if __name__ == '__main__':
    main()
