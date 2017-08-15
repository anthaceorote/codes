def permute(s):
    ''' Generator which yields all permutations of string s '''
    return permutation("", s)


def permutation(ans, remain):
    if not remain:
        # print(ans)
        yield ans
    else:
        for i, ch in enumerate(remain):
            new_remain = remain[:i] + remain[i + 1:]
            if ch in remain[i + 1:]:
                continue
            yield from permutation(ans + ch, new_remain)


def isPermutation(a, b):
    ''' 
        Returns True if b is a valid permutation of a 
        Assumptions:    No spaces - in between, leading, or trailing
                        All small case letters
    '''
    if len(a) != len(b):
        return False
    charCount = [0] * 26
    for ch in a:
        charCount[ord(ch) - 97] += 1
    for ch in b:
        charCount[ord(ch) - 97] -= 1
        if charCount[ord(ch) - 97] < 0:
            return False
    return True


if __name__ == '__main__':
    s = 'dood'
    print("All permutations of string {} - ".format(s))
    for i, p in enumerate(permute(s), 1):
        print(i, p)

    a = "dog"
    b = "god"
    print("\na = {}, b = {}".format(a, b))
    print("isPermutation(a,b) =", isPermutation(a, b))
