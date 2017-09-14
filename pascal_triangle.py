
def get_next(n):
    ''' Generate next row in Pascal's triangle by adding two consecutive digits '''
    n = n.split()
    next_num = []
    for i in range(len(n) - 1):
        # next_num.append(str(int(n[i]) + int(n[i + 1])))
        next_num.append(int(n[i]) + int(n[i + 1]))
    return ' '.join(next_num)


def print_val(values):
    ''' Print Pascal's Triangle with Proper spacing on either side '''
    max_len = len(str(max(values, key=lambda x: len(str(x)))))
    # print(max_len)
    for val in values:
        print('{0: ^{l}}'.format(str(val), l=max_len))


def pascal_triangle(n):
    ''' Generating Pascal Triangle for asked number of rows '''
    values = ['1', '1 1']

    if n < 3:
        print_val(values[:n])
    else:
        for _ in range(2, n):
            last_val = values[-1]
            x = get_next(last_val)
            new_val = '1 {} 1'.format(x)
            values.append(new_val)

        print_val(values)


def pascal_triangle2(n_rows):
    ''' Pascal Triangle using zip function '''
    ans = []
    for _ in range(n_rows):
        row = [1]
        if ans:
            last_row = ans[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        ans.append(row)
    # print(ans)
    print_val(ans)


if __name__ == '__main__':
    pascal_triangle2(10)
