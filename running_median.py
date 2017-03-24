# Enter your code here. Read input from STDIN. Print output to STDOUT
class Heap(object):
    def __init__(self):
        self.items = [0]
        
    def __repr__(self):
        return ' '.join(map(str, self.items[1:]))
        
    def size(self):
        return len(self.items)-1

    def isEmpty(self):
        return self.size()==0
    
    def peek(self):
        return self.items[1]
    
    def hasLeftChild(self, idx):
        if 2*idx <= self.size():
            return True
        return False
    
    def getLeftChild(self, idx):
        return self.items[2*idx]
    
    def hasRightChild(self, idx):
        if 2*idx+1 <= self.size():
            return True
        return False
    
    def getRightChild(self, idx):
        return self.items[2*idx + 1]
    
class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)
    
    def buildHeap(self, arr):
        i = len(arr)//2
        self.items.append(arr)
        while i>0:
            self.siftDown(i)
            i -= 1
            
    def insert(self, val):
        self.items.append(val)
        self.siftUp(self.size())
        
    def siftUp(self, idx):
        while idx//2 > 0:
            if self.items[idx//2] > self.items[idx]:
                self.items[idx], self.items[idx//2] = self.items[idx//2], self.items[idx]
                idx //= 2
            else:
                break
                
    def siftDown(self, idx):
        while idx*2 <= self.size():
            if self.hasRightChild(idx):
                if self.items[idx*2] < self.items[idx*2 + 1]:
                    minIdx = idx*2
                else:
                    minIdx = idx*2 + 1
            else:
                minIdx = idx*2
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
        i = len(arr)//2
        self.items.append(arr)
        while i>0:
            self.siftDown(i)
            i -= 1
            
    def insert(self, val):
        self.items.append(val)
        self.siftUp(self.size())
        
    def siftUp(self, idx):
        while idx//2 > 0:
            if self.items[idx//2] <= self.items[idx]:
                self.items[idx], self.items[idx//2] = self.items[idx//2], self.items[idx]
                idx //= 2
            else:
                break
                
    def siftDown(self, idx):
        while idx*2 <= self.size():
            if self.hasRightChild(idx):
                if self.items[idx*2] >= self.items[idx*2 + 1]:
                    minIdx = idx*2
                else:
                    minIdx = idx*2 + 1
            else:
                minIdx = idx*2
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

def add(a):
    global min_heap, max_heap
    if max_heap.isEmpty():
        max_heap.insert(a)
    elif max_heap.size() == min_heap.size():
        if max_heap.peek() < a:
            min_heap.insert(a)
            max_heap.insert(min_heap.delMin())
        else:
            max_heap.insert(a)
    else: # elif max_heap.size() > min_heap.size():
        if max_heap.peek() < a:
            min_heap.insert(a)
        else:
            max_heap.insert(a)
            min_heap.insert(max_heap.delMax())

def getMedian():
    global min_heap, max_heap
    if max_heap.size() > min_heap.size():
        return max_heap.peek()
    else:
        return (max_heap.peek() + min_heap.peek()) / 2.0;

if __name__ == "__main__":
    '''
        Question: https://www.hackerrank.com/challenges/find-the-running-median
        Use two heaps - a MinHeap and a MaxHeap - to store the data stream
        Use MinHeap to store the "Maximum" elements (elements to the right of the median)
        Use MaxHeap to store the "Minimum" elements (elements to the left of the median)
        Start with MaxHeap; always maintain MaxHeap to be of equal or one element bigger than MinHeap
        Hence,  the median is either root of MaxHeap (odd number of entries) 
                or average of roots of Min and Max heap (even number of entries)
    '''
    
    global min_heap, max_heap
    min_heap, max_heap = MinHeap(), MaxHeap()
    inp = range(1,11)
    for a in inp:
        add(a)
        ans = getMedian()
        print("%.1f" % ans)