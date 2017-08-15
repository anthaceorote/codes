def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    ans = x
    while ans * ans > x:
        ans = (ans + x / ans) // 2
    if not (ans**2 <= x <= (ans + 1)**2):
        print(x)
    return ans


for i in range(1000000):
    mySqrt(i)
