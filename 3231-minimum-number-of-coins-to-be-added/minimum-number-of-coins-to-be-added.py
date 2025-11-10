class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        added = 0
        reach = 0
        ar = []
        for c in coins:
            if reach >= target:
                return added

            while reach + 1 < c:
                added += 1
                reach += (reach + 1)
            reach += c
        
        while reach + 1 <= target:
            added += 1
            reach += (reach + 1)
        return added
            