def reverse_number(n):
    ans = 0
    while n != 0:
        r = n % 10
        n = n // 10
        ans = ans * 10 + r
    return ans

if __name__ == '__main__':
    assert reverse_number(193) == 391, '391'
    assert reverse_number(12331) == 13321, '13321'
    assert reverse_number(1) == 1, '1'
