def convert_decimal(n, base):
    if n == 0:
        return 0
    digits = '0123456789ABCDEF'
    remainders = []
    while n != 0:
        r = n % base
        n = n // base
        remainders.append(r)
        # print(r, n, remainders)
    return ''.join(digits[r] for r in reversed(remainders))


def convert_to_decimal(n, base):
    if n == 0:
        return 0
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    ans = 0
    power = 0
    while n:
        ans = ans + digits[n[-1]] * (base ** power)
        n = n[:-1]
        power += 1
    return ans

if __name__ == '__main__':
    assert convert_decimal(10, 2) == '1010', '1010'
    assert convert_decimal(10, 16) == 'A', 'A'
    assert convert_decimal(10, 10) == '10', '10'

    assert convert_to_decimal('1010', 2) == 10, '10'
    assert convert_to_decimal('ABCDE', 16) == 703710, '703710'
    assert convert_to_decimal('ABCDE', 15) == 546284, '546284'
