class RecentCounter:

    def __init__(self):
        self.req = deque()
        

    def ping(self, t: int) -> int:
        l = t - 3000
        self.req.append(t)
        while self.req and self.req[0] < l:
            self.req.popleft()
        return len(self.req)
            

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)