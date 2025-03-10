class MyQueue:

    def __init__(self):
        self.stack = []
        self.headIdx = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        x = self.stack[self.headIdx]
        self.headIdx += 1
        return x
        
    def peek(self) -> int:
        return self.stack[self.headIdx]
        

    def empty(self) -> bool:
        return len(self.stack) <= self.headIdx
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()