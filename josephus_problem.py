'''
https://en.wikipedia.org/wiki/Josephus_problem
http://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
'''


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return self.queue


def josephus_problem(n, interval):
    q = Queue()
    for i in range(1, n + 1):
        q.enqueue(i)

    dead = []
    while len(q) > 1:
        for i in range(interval - 1):
            q.enqueue(q.dequeue())
        dead.append(q.dequeue())

    return q.dequeue()


def josephus_recursive(n, k):
    # Base case: 	If there is only one person in circle, he survives
    # Recursion: 	After the first person is killed (kth from beginning), there are n-1 people left.
    # Hence, we call josephus(n-1, k). But this assumes starting position to be (k % n + 1), ie one person after kth person.
    # We offset this by counting the (k-1) survivors again.
    if n == 1:
        return 1
    else:
        return (josephus_recursive(n - 1, k) + k - 1) % n + 1

if __name__ == '__main__':
    assert josephus_problem(50, 7) == 1, '1'
    assert josephus_recursive(50, 7) == 1, '1'
