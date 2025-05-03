class MedianFinder:

    def __init__(self):
        self.min_heap = [] # used to collect the right half
        self.max_heap = [] # used to collect the left half
        
    def addNum(self, num: int) -> None:
        heappush(self.max_heap, - num)
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heappush(self.min_heap, - heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, - heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()