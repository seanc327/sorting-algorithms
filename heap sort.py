# functions: push peek pop
# private functions: _up _down (_swap removed because i just implemented it in up/down)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, n):
        self.heap.append(n)
        self._up(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._down(0)
        return root

    def _up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index] > self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]

    def _down(self, index):
        l = index * 2 + 1
        r = index * 2 + 2
        largest = index
        if len(self.heap) > l and self.heap[l] > self.heap[largest]:
            largest = l
        if len(self.heap) > r and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != index:
            self._down(largest)
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]

if __name__ == '__main__':
    # test
    maxheap = MaxHeap()
    maxheap.push(2)
    maxheap.push(12)
    maxheap.push(34)
    maxheap.push(72)
    maxheap.push(22)
    maxheap.push(36)
    maxheap.push(18)
    maxheap.push(8)
    maxheap.push(3)

    print(maxheap.heap) # expected: [34, 72, 36, 8, 22, 12, 18, 2, 3]
    print(maxheap.pop()) # expected: 34
    print(maxheap.heap) # expected: [72, 3, 36, 8, 22, 12, 18, 2]
    print(maxheap.peek()) # expected: 72
