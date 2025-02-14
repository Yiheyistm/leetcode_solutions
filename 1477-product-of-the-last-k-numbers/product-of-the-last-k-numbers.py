class ProductOfNumbers:

    def __init__(self):
        self.product_lst = []

    def add(self, num: int) -> None:
        if len(self.product_lst) == 0 and num != 0:
            self.product_lst.append(num)
            return
        if num == 0:
           self.product_lst = [] 
        else:
            prev = self.product_lst[-1]
            self.product_lst.append(num * prev)
    def getProduct(self, k: int) -> int:
        if len(self.product_lst) < k:
            return 0
        elif len(self.product_lst) == k:
            return self.product_lst[-1]
        else:
            return self.product_lst[-1] // self.product_lst[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)