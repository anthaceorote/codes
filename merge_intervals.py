class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

    def __eq__(self, other):
        return (self.start == other.start) and (self.end == other.end)


def merge_intervals(intervals):
    '''
    :type intervals: List[Interval]
    :rtype: List[Interval]

    Source: https://leetcode.com/problems/merge-intervals/description/
    Given a collection of intervals, merge all overlapping intervals.

    Approach:
    Sort the intervals based on (start_time, end_time).
    This guarantees that you will get intervals which start first, 
    and if two intervals start at the same time, then you will get interval which ends first, first.
    Traverse through this sorted interval list, and find out if two consecutive intervals overlap,
    by comparing the end of the prior one to start time of the next.
    '''
    intervals.sort(key=lambda i: (i.start, i.end))
    result = []
    prev = intervals[0]
    for i in range(1, len(intervals)):
        next_iv = intervals[i]
        if next_iv.start > prev.end:
            result.append(prev)
            prev = next_iv
        else:
            prev.end = max(prev.end, next_iv.end)
    result.append(prev)
    return result


if __name__ == '__main__':
    interval_list = [Interval(1, 3), Interval(2, 5), Interval(5, 8), Interval(10, 15), Interval(20, 22)]
    assert merge_intervals(interval_list) == [Interval(1, 8), Interval(10, 15), Interval(20, 22)]
