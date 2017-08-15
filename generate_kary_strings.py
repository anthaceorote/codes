def rangeToList(k):
    result = [str(i) for i in range(0, k)]
    return result


def generate_kary_strings(n, k):
    ''' Generates k-ary strings consisting of [0, 1, ... k-1] numbers of 'n' digits
        e.g.    generate_kary_strings(2,2) --> ['00', '01', '10', '11']
                generate_kary_strings(3,2) --> ['000', '001', '010', '011', '100', '101', '110', '111']
                generate_kary_strings(2,3) --> ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    '''
    if n == 0:
        yield 0
    elif n == 1:
        yield from rangeToList(k)
    else:
        yield from (digit + bitstring for digit in generate_kary_strings(1, k) for bitstring in generate_kary_strings(n - 1, k))


if __name__ == '__main__':
    assert list(generate_kary_strings(4, 2)) == ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
