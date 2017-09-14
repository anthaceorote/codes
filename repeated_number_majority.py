def repeatedNumber(nums, majority):
    '''
    :type nums: List[int]
    :type majority: int
    :rtype: int

    Source: https://leetcode.com/problems/majority-element/description/

    Given an array of size n, find the majority element.
    The majority element is the element that appears more than floor(n/majority) times.

    Approach:
    While itering over the given list, if you keep count of the candidate 'majority' nums, 
    the answer is bound to be one of the candidates.

    So for each number in the list - 
    (1) See if it is one of the candidates; if yes, then increase the corr count
    (2) Else, replace the first candidate with count 0
    (3) If no candidate has count zero, then decrease all counts by 1

    After this, you should have the majority elements in candidate array.
    Iterate over the candidates, and get their final counts.
    Check the maximum of the counts against the thresholds to identify the answer.
    '''

    # Storing the candidate for top occuring numbers and their counts
    candidate_nums = [0] * (majority - 1)
    num_counts = [0] * (majority - 1)

    for n in nums:
        for i, c in enumerate(candidate_nums):
            if n == c:
                num_counts[i] += 1
                break
        else:
            for i, cnt in enumerate(num_counts):
                if cnt == 0:
                    candidate_nums[i] = n
                    num_counts[i] = 1
                    break
            else:
                for i in range(len(num_counts)):
                    num_counts[i] -= 1

    verify_counts = [0] * (majority - 1)

    for n in nums:
        try:
            idx = candidate_nums.index(n)
            verify_counts[idx] += 1
        except:
            pass

    threshold = len(nums) // majority

    # print(candidate_nums, verify_counts)
    max_count = max(verify_counts)
    if max_count > threshold:
        return candidate_nums[verify_counts.index(max_count)]

    return -1


if __name__ == '__main__':
    arr = [1000727, 1000727, 1000641, 1000517, 1000212, 1000532, 1000727, 1001000, 1000254, 1000106, 1000405, 1000100, 1000736, 1000727, 1000727, 1000787, 1000105, 1000713, 1000727, 1000333, 1000069, 1000727, 1000877, 1000222, 1000727, 1000505, 1000641, 1000533, 1000727, 1000727, 1000727, 1000508, 1000475, 1000727, 1000573, 1000727, 1000618, 1000727, 1000309, 1000486, 1000792, 1000727, 1000727, 1000426, 1000547, 1000727, 1000972, 1000575, 1000303, 1000727, 1000533, 1000669, 1000489, 1000727, 1000329, 1000727, 1000050, 1000209, 1000109]
    # from collections import Counter
    # print(arr, Counter(arr))
    assert repeatedNumber(arr, 3) == 1000727
    assert repeatedNumber(arr, 2) == -1
    assert repeatedNumber([1, 2, 3], 3) == -1

'''
For number with n/3 majority

    first, second = None, None
    first_count, second_count = 0, 0
    if n == first:
        first_count += 1
    elif n == second:
        second_count += 1
    elif first_count == 0:
        first, first_count = n, 1
    elif second_count == 0:
        second, second_count = n, 1
    else:
        first_count -= 1
        second_count -= 1

    t_first_count, t_second_count = 0, 0
    for n in nums:
        if n == first:
            t_first_count += 1
        elif n == second:
            t_second_count += 1

    threshold = len(nums) // 3
    if t_first_count > t_second_count:
        if t_first_count > threshold:
            return first

    if t_second_count > t_first_count:
        if t_second_count > threshold:
            return second
'''
