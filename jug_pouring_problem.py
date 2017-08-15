'''
Link: http://www.geeksforgeeks.org/two-water-jug-puzzle/

Two water jugs of size 'p' and 'q' litres each (0 < p < q)
Target is to measure 't' litres of water (t < q)
Find out the minimum number of operations required to do this
'''


class Cup:

    def __init__(self, capacity=1, contents=0):
        if capacity < contents:
            raise ValueError('Overfilled')
        if contents < 0:
            raise ValueError('Negative Content?!')
        self.capacity = capacity
        self.contents = contents
        self.moves = 0

    @property
    def space(self):
        return self.capacity - self.contents

    @property
    def is_empty(self):
        return self.space == self.capacity

    @property
    def is_full(self):
        return self.contents == self.capacity

    def is_goal(self, goal):
        return self.contents == goal

    def __eq__(self, other):
        return self.capacity == other.capacity and self.contents == other.contents

    def pour_into(self, other):
        self.contents, other.contents = self.contents - min(self.contents, other.space), other.contents + min(self.contents, other.space)
        self.moves += 1
        return self, other

    def refill(self):
        self.contents = self.capacity
        self.moves += 1

    def empty(self):
        self.contents = 0
        self.moves += 1

    def __repr__(self):
        return '{}(capacity={}, contents={})'.format(self.__class__.__name__, self.capacity, self.contents)

    def __str__(self):
        return "<Cup {}/{}>".format(self.contents, self.capacity)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def pour(cup1, cup2, goal):
    print("Initial State ", cup1, cup2)
    while not cup1.is_goal(goal) or not cup2.is_goal(goal):
        cup1, cup2 = cup1.pour_into(cup2)
        print(cup1, cup2)
        if cup1.is_goal(goal) or cup2.is_goal(goal):
            break
        if cup1.is_empty:
            cup1.refill()
            print(cup1, cup2)
        if cup2.is_full:
            cup2.empty()
            print(cup1, cup2)

    print(cup1.moves + cup2.moves, '\n')
    return cup1.moves + cup2.moves


def min_steps(first, second, target):
    if first > second:
        first, second = second, first

    if target > second:
        raise ValueError('Expecting Over Capacity')

    if (target % gcd(second, first) != 0):
        return -1

    return min(pour(Cup(second, second), Cup(first, 0), target),
               pour(Cup(first, first), Cup(second, 0), target))

if __name__ == '__main__':
    print(min_steps(5, 3, 4))
