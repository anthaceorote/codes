def print_mat(m, word1, word2):
    print('    ' + ' '.join(word2))
    word1 = ' ' + word1
    for i, row in enumerate(m):
        print(word1[i] + ' ' + ' '.join(str(e) for e in row))
    print()


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    s1 = list(word1)
    s2 = list(word2)
    l1, l2 = len(s1), len(s2)
    mat = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0:
                mat[i][j] = j
            elif j == 0:
                mat[i][j] = i

            elif s1[i - 1] == s2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1]
            else:
                mat[i][j] = 1 + min(mat[i][j - 1], mat[i - 1][j], mat[i - 1][j - 1])

    print_mat(mat, word1, word2)
    return mat[l1][l2]


if __name__ == "__main__":
    word1 = 'sunday'
    word2 = 'saturday'
    print(minDistance(word1, word2))
