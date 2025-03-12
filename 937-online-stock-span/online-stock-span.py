# we can solve this problems by using monotonic increasing stack and the span of previous element for the next
#privous price's span less than current price is also the span of current price
class StockSpanner:

    def __init__(self):
        self.stack = [] # [price, span]        

    def next(self, price: int) -> int:
        span = 1 # every price is equal itself
        for p in self.stack:
            while self.stack and self.stack[-1][0] <= price:
                _, s = self.stack.pop() 
                span += s
        self.stack.append([price, span])
        return self.stack[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)