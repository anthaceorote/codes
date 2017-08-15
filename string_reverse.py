def reverse(s):
    ''' Reverses given string s '''
    return ''.join(reversed(s))


def reverse_sentence(sentence):
    ''' Reverses order of words in a sentence '''
    return ' '.join(reversed(sentence.split(" ")))


if __name__ == '__main__':
    a = "some_string"
    b = "this is a sentence"

    print("a = {}, b = {}".format(a, b))
    print("reverse(a) =", reverse(a))
    print("reversed_sentence(b) =", reverse_sentence(b))
    print("Reversed sentence with words reveresed =", reverse(b))
