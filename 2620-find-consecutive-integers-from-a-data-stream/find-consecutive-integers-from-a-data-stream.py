class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.k = k
        self.val = value      

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num != self.val:
            self.stream = []
        return len(self.stream) >= self.k

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)