class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()            
        reach = 0
        for c in coins:
            if reach + 1 < c: break
            reach += c
        return reach + 1
            


        

        