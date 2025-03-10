class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.head = None
        self.tail = None        

    def insertFront(self, value: int) -> bool:
        if self.size == 0:
            return False
        node = Node(val = value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == 0:
            return False
        node = Node(val = value)
        if not self.head:
            self.insertFront(value)
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.size -= 1
        return True
        

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        if self.tail == self.head:
            self.head = self.tail = None
            self.size += 1
            return True
        self.head = self.head.next
        self.head.pre = None
        self.size += 1
        return True
        
    def deleteLast(self) -> bool:
        if not self.head or not self.tail:
            return False
        if self.tail == self.head:
            self.head = self.tail = None
            self.size += 1
            return True
        self.tail = self.tail.prev
        self.tail.next = None
        self.size += 1
        return True
        

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val        

    def getRear(self) -> int:
        if not self.head or not self.tail:
            return -1
        return self.tail.val
        
    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False        

    def isFull(self) -> bool:
        return self.size == 0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()