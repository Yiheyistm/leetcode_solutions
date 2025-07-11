class SmallestInfiniteSet:

    def __init__(self):
        self.st = set(list(range(1,2000)))
        self.heap = list(range(1, 2000))
        heapify(self.heap)
        

    def popSmallest(self) -> int:
        pop = heappop(self.heap)
        self.st.remove(pop)
        return pop

    def addBack(self, num: int) -> None:
        if num not in self.st:
            heappush(self.heap, num)
            self.st.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)