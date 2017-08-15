'''

    Sort a list of non-negative integers so that,
    if the integers were converted to string, concatenated and converted back to int, 
    the resulting int is the highest possible for that list

    Source:
    https://leetcode.com/problems/largest-number/description/
    http://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

'''

from fractions import Fraction
from functools import cmp_to_key


def largest_number(x):
    '''
    input: list of integers, x
    output: max number that can be formed ordering the integers from the list x

    e.g.: x = [9, 30, 14, 3, 1]
    some numbers that can be formed include -
    9301431 (appending numbers in order), 3014931 (sorting in descending order), 9303141 (sorting in descending after appending zeroes at end to make length equal), etc
    but max num that can be formed is: 9330141

    algorithm:
    proper_order_1 :- https://stackoverflow.com/a/30189892/5774864

    proper_order_2 :-
    while sorting, use this modified comparator:
        if ab > ba, pick a before b, else b before a

    '''

    def cmp_func(a, b):
        a, b = str(a), str(b)
        ab, ba = a + b, b + a
        if ab == ba:
            return 0
        if ab < ba:
            return -1
        return 1

    proper_order_1 = sorted(x, reverse=True, key=lambda n: Fraction(n, 10**len(str(n)) - 1))
    proper_order_2 = sorted(x, reverse=True, key=cmp_to_key(cmp_func))

    assert proper_order_1 == proper_order_2

    max_num = int(''.join(str(x) for x in proper_order_1))
    return max_num


def main():
    assert largest_number([9, 30, 14, 1, 3]) == 9330141
    assert largest_number([3, 2, 12, 0, 5, 14]) == 53214120
    assert largest_number([9, 32, 10, 1, 3]) == 9332110
    assert largest_number([50, 5, 51, 59, 2, 1, 9, 98]) == 998595515021

if __name__ == '__main__':
    main()
