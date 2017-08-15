class Heap(object):
    def __init__(self):
        self.items = [0]

    def __repr__(self):
        return ' '.join(map(str, self.items[1:]))

    def size(self):
        return len(self.items) - 1

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        return self.items[1]

    def hasLeftChild(self, idx):
        if 2 * idx <= self.size():
            return True
        return False

    def getLeftChild(self, idx):
        return self.items[2 * idx]

    def hasRightChild(self, idx):
        if 2 * idx + 1 <= self.size():
            return True
        return False

    def getRightChild(self, idx):
        return self.items[2 * idx + 1]


class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def buildHeap(self, arr):
        i = len(arr) // 2
        self.items.append(arr)
        while i > 0:
            self.siftDown(i)
            i -= 1

    def insert(self, val):
        self.items.append(val)
        self.siftUp(self.size())

    def siftUp(self, idx):
        while idx // 2 > 0:
            if self.items[idx // 2] > self.items[idx]:
                self.items[idx], self.items[idx // 2] = self.items[idx // 2], self.items[idx]
                idx //= 2
            else:
                break

    def siftDown(self, idx):
        while idx * 2 <= self.size():
            if self.hasRightChild(idx):
                if self.items[idx * 2] < self.items[idx * 2 + 1]:
                    minIdx = idx * 2
                else:
                    minIdx = idx * 2 + 1
            else:
                minIdx = idx * 2
            if self.items[idx] > self.items[minIdx]:
                self.items[idx], self.items[minIdx] = self.items[minIdx], self.items[idx]
                idx = minIdx
            else:
                break

    def delMin(self):
        minItem = self.items[1]
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        _ = self.items.pop()
        self.siftDown(1)
        return minItem

    def delete(self, val):
        eleIdx = self.items.index(val)
        self.items[eleIdx] = self.items[-1]
        self.items.pop()
        self.siftDown(eleIdx)

    def getMin(self):
        return self.items[1]


class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def buildHeap(self, arr):
        i = len(arr) // 2
        self.items.append(arr)
        while i > 0:
            self.siftDown(i)
            i -= 1

    def insert(self, val):
        self.items.append(val)
        self.siftUp(self.size())

    def siftUp(self, idx):
        while idx // 2 > 0:
            if self.items[idx // 2] <= self.items[idx]:
                self.items[idx], self.items[idx // 2] = self.items[idx // 2], self.items[idx]
                idx //= 2
            else:
                break

    def siftDown(self, idx):
        while idx * 2 <= self.size():
            if self.hasRightChild(idx):
                if self.items[idx * 2] >= self.items[idx * 2 + 1]:
                    minIdx = idx * 2
                else:
                    minIdx = idx * 2 + 1
            else:
                minIdx = idx * 2
            if self.items[idx] <= self.items[minIdx]:
                self.items[idx], self.items[minIdx] = self.items[minIdx], self.items[idx]
                idx = minIdx
            else:
                break

    def delMax(self):
        maxItem = self.items[1]
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        _ = self.items.pop()
        self.siftDown(1)
        return maxItem

    def delete(self, val):
        eleIdx = self.items.index(val)
        self.items[eleIdx] = self.items[-1]
        self.items.pop()
        self.siftDown(eleIdx)

    def getMax(self):
        return self.items[1]
