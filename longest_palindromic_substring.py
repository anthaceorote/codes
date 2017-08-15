def longest_palindromic_substring(s):
    max_length = 1

    start = 0
    str_len = len(s)

    low, high = 0, 0

    for i in range(str_len):

        low = i - 1
        high = i
        while low >= 0 and high < str_len and s[low] == s[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low -= 1
            high += 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < str_len and s[low] == s[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low -= 1
            high += 1

    return s[start: start + max_length]

for s in ["abbc", "abcde", "abbccbb", "abcbade", "thisshit"]:
    print(longest_palindromic_substring(s))
