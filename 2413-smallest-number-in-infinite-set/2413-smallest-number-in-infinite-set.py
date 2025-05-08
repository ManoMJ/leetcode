class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        for i in range(1,1001):
            self.heap.append(i)

    def popSmallest(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        minimum = self.heap.pop()
        index = 0
        child = index*2 + 1
        while child < len(self.heap):
            right = child + 1
            if right < len(self.heap) and self.heap[right] < self.heap[child]:
                child = right
            if self.heap[index] < self.heap[child]:
                break
            self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
            index = child
            child = index * 2 + 1
        return minimum

    def addBack(self, num: int) -> None:
        if num in self.heap:
            return

        self.heap.append(num)
        index=len(self.heap)-1
        parent = (index-1)//2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index-1)//2


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)