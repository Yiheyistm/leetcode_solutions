class Node:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        cnt = 0
        while curr:
            if cnt == index:
                return curr.val
            curr = curr.next
            cnt += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
            node = Node(val)
            if not self.head:
                self.head = node
            else:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = node
            
        

    def addAtIndex(self, index: int, val: int) -> None:       
            node = Node(val)
            if index == 0:
                self.addAtHead(val)
                return

            curr = self.head
            for _ in range(index - 1):
                if not curr or not curr.next:
                    return
                curr = curr.next
            if curr:
                node.next = curr.next
                curr.next = node
           

    def deleteAtIndex(self, index: int) -> None:
            curr = self.head
            if index == 0 and curr:
                self.head = curr.next
                return
            
            for _ in range(index - 1):
                if not curr:
                    return
                curr = curr.next
            if curr and curr.next:
                curr.next = curr.next.next       


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)