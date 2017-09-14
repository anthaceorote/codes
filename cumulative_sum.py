def cumulative_sum(lst):
    total = 0
    for x in lst:
        yield total
        total += x
    yield total


if __name__ == '__main__':
    assert list(cumulative_sum([1, 2, 3, 4, 5])) == [0, 1, 3, 6, 10, 15]
    assert list(cumulative_sum([1] * 5)) == [0, 1, 2, 3, 4, 5]
