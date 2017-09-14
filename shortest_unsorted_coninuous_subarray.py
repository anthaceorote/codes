import sys


def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int

    Source: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
    Given an integer array, find one continuous subarray that if you only sort this subarray in ascending order, 
    then the whole array will be sorted in ascending order, too.
    Find the shortest such subarray and output its length.
    """
    if len(nums) < 2:
        return 0

    left_violation, right_violation = False, False
    unsorted_min, unsorted_max = sys.maxsize, -1 * sys.maxsize

    for i in range(1, len(nums)):
        # Find number from left which breaks the trend/ slope (non-decreasing)
        if nums[i] < nums[i - 1]:
            left_violation = True
        # If trend is broken, keep track of the smallest number you encounter
        if left_violation:
            unsorted_min = min(unsorted_min, nums[i])

    for i in range(len(nums) - 2, -1, -1):
        # Find number from right which breaks the trend/ slope (non-increasing)
        if nums[i] > nums[i + 1]:
            right_violation = True
        # If trend is broken, keep track of the largest number you encounter
        if right_violation:
            unsorted_max = max(unsorted_max, nums[i])

    # Find positions for the unsorted_min and unsorted_max
    # These pointers will indicate the subarray which needs to be sorted for the whole array to be sorted
    left, right = 0, 0

    for left in range(len(nums)):
        if nums[left] > unsorted_min:
            break

    for right in range(len(nums) - 1, -1, -1):
        if nums[right] < unsorted_max:
            break

    return 0 if (right - left < 0) else (right - left + 1)


if __name__ == '__main__':
    assert findUnsortedSubarray([1, 2, 4, 3, 5]) == 2
    assert findUnsortedSubarray(list(range(10))) == 0
    assert findUnsortedSubarray([5, 4, 3, 2, 1]) == 5
    assert findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert findUnsortedSubarray([1]) == 0
