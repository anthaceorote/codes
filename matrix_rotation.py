def display_mat(mat):
    ''' Prints the matrix '''
    for row in mat:
        print('\t'.join(str(ele) for ele in row))


def rotate_mat(mat, anti_clockwise=False):
    ''' Rotate the matrix clock-wise or anti-clockwise '''
    ''' Reference: http://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/ '''
    m = [list(row) for row in mat]
    n = len(m[0])
    if anti_clockwise:
        # return list(map(list, zip(*m)))[::-1]
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = m[i][j]
                m[i][j] = m[j][n - 1 - i]
                m[j][n - 1 - i] = m[n - 1 - i][n - 1 - j]
                m[n - 1 - i][n - 1 - j] = m[n - 1 - j][i]
                m[n - 1 - j][i] = temp
        return m
    else:
        # return list(map(list, zip(*m[::-1])))
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = m[i][j]
                m[i][j] = m[n - 1 - j][i]
                m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j]
                m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i]
                m[j][n - 1 - i] = temp
        return m


def transpose_mat(mat):
    return [list(x) for x in zip(*mat)]


def rotate_matrix(mat, anti_clockwise=False):
    if anti_clockwise:
        m_t = transpose_mat(mat)
        n_row = len(m_t)
        for i in range(n_row // 2):
            m_t[i], m_t[n_row - 1 - i] = m_t[n_row - 1 - i], m_t[i]
    else:
        n_row = len(mat)
        m_t = [list(row) for row in mat]
        for i in range(n_row // 2):
            m_t[i], m_t[n_row - 1 - i] = m_t[n_row - 1 - i], m_t[i]
        m_t = transpose_mat(m_t)
    return m_t


if __name__ == '__main__':
    n = 5
    matrix = [[i for i in range(x * n + 1, (x * n + 1) + n)] for x in range(n)]

    print("Original Matrix:")
    display_mat(matrix)

    print("\nClockwise Rotation:")
    n = rotate_mat(matrix)
    display_mat(n)

    print("\nAnti-Clockwise Rotation:")
    m = rotate_mat(matrix, anti_clockwise=True)
    display_mat(m)

    m, n = 3, 5
    rect_matrix = [[i for i in range(x * n + 1, (x * n + 1) + n)] for x in range(m)]

    print("\nRectangular Matrix:")
    display_mat(rect_matrix)

    print("\nRotating A Rectangular (Non-Square) Matrix Clockwise:")
    m = rotate_matrix(rect_matrix)
    display_mat(m)

    print("\nRotating A Rectangular (Non-Square) Matrix Anti-Clockwise:")
    m = rotate_matrix(rect_matrix, anti_clockwise=True)
    display_mat(m)
