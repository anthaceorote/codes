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


def main():
    assert prime_factors(56) == [2, 2, 2, 7]
    assert prime_factors(203) == [7, 29]


if __name__ == '__main__':
    main()
