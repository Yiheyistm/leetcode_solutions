class Node:
    def __init__(self, val = 0, next = None, prev = None, key = 0):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0
        self.list_map = {}
        

    def get(self, key: int) -> int:
        if key in self.list_map:
            self.update(key)
            return self.list_map[key].val
        return -1
        
    def addAtHead(self, key, node) -> None:
        if not self.head: 
            self.head = node
            self.tail = node  
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node 
        self.list_map[key] = node


    def put(self, key: int, value: int) -> None:
        node = Node(val=value, key=key)
        if not self.head:
            self.addAtHead(key, node)
            self.size += 1
        elif key in self.list_map:
            self.list_map[key].val = value
            self.update(key)
        else:
            if self.size < self.capacity:  # If cache is not full
                self.addAtHead(key, node)
                self.size += 1
            else:
                self.addAtHead(key, node)
                tail_key = self.tail.key
                self.moveTailBack()
                del self.list_map[tail_key]

    def update(self, key) -> None:
            nd = self.list_map[key]
            nd_prev = nd.prev
            nd_next = nd.next
            if nd_next and nd_prev: # If the nd has next pointer and prev pointer
                nd_next.prev = nd_prev
                nd_prev.next = nd_next
            elif not nd_prev: # the nd hasn't prev pointer i.e head
                self.head.val = nd.val
                return
            elif not nd_next: # the nd has not nxt pointer i.e tail
                self.moveTailBack()

            nd.prev = None
            nd.next = self.head
            self.head.prev = nd
            self.head = nd
    def moveTailBack(self):
        if self.tail.prev is None:
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)