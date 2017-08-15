def word_matrix_rotation_90_anticlockwise(mat):
    return list(zip(*mat[::-1]))


if __name__ == '__main__':
    matrix = ['lady', 'gaga', 'dnce', 'hert']
    print(matrix)
    ans = word_matrix_rotation_90_anticlockwise(matrix)
    print([''.join(a) for a in ans])
