def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not word:
        return True

    if not board:
        return False

    def get_occurence(board, letter):
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == letter:
                    yield (i, j)

    letters_used = [[0] * len(board[0]) for _ in range(len(board))]

    def search(board, word, i, j, idx):
        if idx == len(word):
            return True

        if i >= len(board) or i < 0 or j >= len(board[i]) or j < 0 or board[i][j] != word[idx] or letters_used[i][j] == 1:
            return False

        letters_used[i][j] = 1

        if (
            search(board, word, i + 1, j, idx + 1) or
            search(board, word, i - 1, j, idx + 1) or
            search(board, word, i, j + 1, idx + 1) or
            search(board, word, i, j - 1, idx + 1)
        ):
            return True
        else:
            letters_used[i][j] = 0
            return False

    first_char = word[0]

    for x, y in get_occurence(board, first_char):
        if search(board, word, x, y, 0):
            return True

    return False
