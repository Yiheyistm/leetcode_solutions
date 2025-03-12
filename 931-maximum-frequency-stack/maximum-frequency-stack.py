# lets soleve this problem by using hashmap for counting the freq of each num and group each nums based on the number of freq by using stack and track the max freq of the list
# lets get to it :)
class FreqStack:

    def __init__(self):
        self.freq = {} # num and freq map
        self.group = defaultdict(list) # freq with groups
        self.mx = 0 # max freq of the list

    def push(self, val: int) -> None:
        nwVal = 1 + self.freq.get(val, 0)
        self.freq[val] = nwVal
        if nwVal > self.mx:
            self.mx = nwVal
        self.group[nwVal].append(val)        
    
    def pop(self) -> int:
        val = self.group[self.mx].pop()
        self.freq[val] -= 1
        if not self.group[self.mx]:
            del self.group[self.mx]
            self.mx -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()