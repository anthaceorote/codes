def getVal(A, i, j, L, H):
    if (i < 0 or i >= L or j < 0 or j >= H):
        return 0
    else:
        return A[i][j]


def findMaxBlock(A, r, c, L, H, size):
    global maxsize
    global countArray
    if r >= L or c >= H:
        return
    countArray[r][c] = 1
    size += 1
    if size > maxsize:
        maxsize = size

    # Search in all 8 directions from current block
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    for x, y in directions:
        new_i, new_j = r + x, c + y
        val = getVal(A, new_i, new_j, L, H)
        if val > 0 and countArray[new_i][new_j] == 0:
            findMaxBlock(A, new_i, new_j, L, H, size)

    countArray[r][c] = 0


def getMaxOnes(A, rowmax, colmax):
    global maxsize
    global size
    global countArray

    for i in range(0, rowmax):
        for j in range(0, colmax):
            if A[i][j] == 1:
                findMaxBlock(A, i, j, rowmax, colmax, 0)

    return maxsize


def display_mat(mat):
    ''' Prints the matrix '''
    for row in mat:
        print('\t'.join(str(ele) for ele in row))


def get_contiguous_area(matrix, output=0):
    global rowmax
    global colmax
    global countArray
    global maxsize
    global size

    mat = matrix
    rowmax = len(mat[0])
    colmax = len(mat)
    maxsize = 0
    size = 0
    countArray = [[0] * colmax for _ in range(rowmax)]

    ans = getMaxOnes(mat, rowmax, colmax)
    if output:
        display_mat(mat)
        print("Number of max contiguous 1s is:", ans)
    return ans

if __name__ == '__main__':
    countArray = [[]]
    rowmax, colmax = 0, 0
    maxsize = 0
    size = 0

    matrix = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 1, 1], [0, 1, 0, 1, 1]]
    assert get_contiguous_area(matrix) == 7, '7'

    matrix = [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 1]]
    assert get_contiguous_area(matrix) == 5, '5'
