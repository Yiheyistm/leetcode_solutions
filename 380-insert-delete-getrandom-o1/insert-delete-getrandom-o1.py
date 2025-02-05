import random
class RandomizedSet:

    def __init__(self):
        self.lst = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst[val] = val
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.lst:
            del self.lst[val]
            return True
        return False
        

    def getRandom(self) -> int:
        a = random.choice(list(self.lst.keys()))

        return a
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()