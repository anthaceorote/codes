def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]

    Source: https://leetcode.com/problems/next-permutation/description/

    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it rearranges as the lowest possible order (ie, sorted in ascending order)
    """
    n = len(nums)
    if n < 2:
        return nums

    # Starting from right, find first index where value decreases
    idx = n - 1
    while idx > 0:
        if nums[idx] > nums[idx - 1]:
            break
        idx -= 1

    # If the number is increasing all the way from right --> left, that is the maximum possible permutation
    # Reset it to the lowest possible order (sorted in ascending)
    if idx == 0:
        nums.sort()
        return nums

    # Find a digit which is just greater than the digit where the rule broke
    val = nums[idx - 1]
    j = n - 1
    while j >= idx:
        if nums[j] > val:
            break
        j -= 1

    # Swap the two digits
    nums[j], nums[idx - 1] = nums[idx - 1], nums[j]

    # Sort the new array in ascending order (just reverse it as it is already in descending order)
    start, end = idx, n - 1
    for i in range(start, (end + start) // 2 + 1):
        nums[i], nums[start + end - i] = nums[start + end - i], nums[i]

    return nums


if __name__ == '__main__':
    assert nextPermutation([1, 2, 3, 4]) == [1, 2, 4, 3]
    assert nextPermutation([3, 2, 4, 1]) == [3, 4, 1, 2]
    assert nextPermutation([4, 3, 2, 1]) == [1, 2, 3, 4]
