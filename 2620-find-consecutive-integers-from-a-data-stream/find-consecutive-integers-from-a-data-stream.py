class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.diffIdx = None
        self.kVAL = k
        self.val = value      

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num != self.val:
            self.diffIdx = len(self.stream)-1
        if len(self.stream) >= self.kVAL:
            if self.diffIdx == None: 
                return True
            elif self.diffIdx != None and (len(self.stream) - self.diffIdx > self.kVAL):
                return True
        return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)