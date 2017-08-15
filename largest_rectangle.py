def largest_rectangle_area(arr):
    stk = []
    i = 0
    max_area = 0

    while i < len(arr):
        if not stk or (arr[i] > arr[stk[-1]]):
            stk.append(i)
        else:
            height = arr[stk.pop()]
            width = i if not stk else (i - stk[-1] - 1)
            max_area = max(max_area, width * height)
            i -= 1
        i += 1

    while stk:
        height = arr[stk.pop()]
        width = i if not stk else (i - stk[-1] - 1)
        max_area = max(max_area, width * height)

    return max_area
