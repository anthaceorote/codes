def spiral_matrix(mat):
    """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Source: https://leetcode.com/problems/spiral-matrix/description/
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
    """
    m, n = len(mat), len(mat[0])
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    direction = 0
    ans = []

    while (top <= bottom) and (left <= right):
        if direction == 0:
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])
            left += 1
        direction = (direction + 1) % 4

    return ans


def spiral_generator(n):
    """
        :type n: int
        :rtype: List[List[int]]

        Source: https://leetcode.com/problems/spiral-matrix-ii/description/
        Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
    """
    def lazy_integer():
        ''' Integer generator '''
        i = 0
        while True:
            i += 1
            yield i

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    direction = 0
    ans = [[0] * n for _ in range(n)]
    int_generator = lazy_integer()

    while (top <= bottom) and (left <= right):
        if direction == 0:
            for i in range(left, right + 1):
                ans[top][i] = next(int_generator)
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                ans[i][right] = next(int_generator)
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                ans[bottom][i] = next(int_generator)
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                ans[i][left] = next(int_generator)
            left += 1
        direction = (direction + 1) % 4

    return ans


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_matrix(mat) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    mat = [[1, 2, 3], [6, 5, 4]]
    assert spiral_matrix(mat) == [1, 2, 3, 4, 5, 6]

    assert spiral_generator(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
