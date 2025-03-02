class History:
    def __init__(self,url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = History(homepage)
        self.currentpage = self.homepage        
    def visit(self, url: str) -> None:
        history = History(url)
        self.currentpage.next = history
        history.prev = self.currentpage
        self.currentpage = self.currentpage.next  

    def back(self, steps: int) -> str:
        curr = self.currentpage
        for _ in range(steps):
            if not curr.prev: break
            curr = curr.prev
        self.currentpage = curr
        return self.currentpage.url
        

    def forward(self, steps: int) -> str:
        curr = self.currentpage
        for _ in range(steps):
            if not curr.next: break
            curr = curr.next
        self.currentpage = curr
        return self.currentpage.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)