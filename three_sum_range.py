'''
Triplets with sum between given range
Problem: https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/
Solution: https://stackoverflow.com/a/19558811/5774864

Take a look at the stock overflow explanation for details and examples
'''
import heapq


def three_sum_range(nums):
    '''
    Given an array of real numbers greater than zero, 
    find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2
    '''

    class Limits:
        ''' Represents ranges '''

        def __init__(self, lower, upper, lower_closed=True, upper_closed=True):
            self.lower = lower
            self.upper = upper
            self.lower_closed = lower_closed
            self.upper_closed = upper_closed

        def in_range(self, num):
            if self.lower_closed:
                if self.upper_closed:
                    return self.lower <= num <= self.upper
                else:
                    return self.lower <= num < self.upper
            else:
                if self.upper_closed:
                    return self.lower < num <= self.upper
                else:
                    return self.lower < num < self.upper

        def __repr__(self):
            return '{}{},{}{}'.format('[' if self.lower_closed else '(', self.lower, self.upper, ']' if self.upper_closed else ')')

    lim_x = Limits(0, 2 / 3, lower_closed=False, upper_closed=False)
    lim_y = Limits(2 / 3, 1, lower_closed=True, upper_closed=True)
    lim_z = Limits(1, 2, lower_closed=False, upper_closed=False)

    X, Y, Z = [], [], []
    for n in nums:
        n = float(n)
        if lim_x.in_range(n):
            heapq.heappush(X, n)
        elif lim_y.in_range(n):
            heapq.heappush(Y, n)
        elif lim_z.in_range(n):
            heapq.heappush(Z, n)

    x_max = heapq.nlargest(3, X)
    x_min = heapq.nsmallest(2, X)
    y_max = heapq.nlargest(1, Y)
    y_min = heapq.nsmallest(2, Y)
    z_min = heapq.nsmallest(1, Z)

    tests = [
        "len(X) >= 3 and sum(x_max) >= 1",
        "len(X) >= 2 and len(Z) >= 1 and sum([x_min[0], x_min[1], z_min[0]]) <= 2",
        "len(X) >= 1 and len(Y) >= 2 and sum([x_min[0], y_min[0], y_min[1]]) <= 2",
        "len(X) >= 1 and len(Y) >= 1 and len(Z) >= 1 and sum([x_min[0], y_min[0], z_min[0]]) <= 2",
        "len(X) >= 2 and len(Y) >= 1 and 1 < sum([x_max[0], x_max[1], y_min[0]]) < 2",
        "len(X) >= 2 and len(Y) >= 1 and 1 < sum([x_min[0], x_min[1], y_max[0]]) < 2",
    ]

    for test in tests:
        if eval(test):
            return True

    return False


if __name__ == '__main__':
    assert three_sum_range([0.6, 0.7, 0.8, 1.2, 0.4]) == True
    assert three_sum_range([0.1] * 5) == False
    assert three_sum_range([2.673662, 2.419159, 0.573816, 2.454376, 0.403605, 2.503658, 0.806191]) == True
    assert three_sum_range([0.002804, 0.000298, 0.748024, 0.139023, 0.082317, 0.013348, 4.20949, 0.098512, 0.055635, 0.060427, 3.290499, 0.073212, 0.071914, 0.065654, 0.044422, 0.024968, 0.110226, 0.090197, 0.06024, 0.100432, 0.10992, 0.023673, 0.081927, 0.066987, 0.058557, 0.043674, 0.057256, 0.050478, 0.024976, 0.048124, 0.071043, 0.048199, 0.023894, 0.058934, 0.047465, 0.088664, 0.002571, 0.070546, 0.042776]) == False
