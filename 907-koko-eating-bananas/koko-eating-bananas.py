class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(k):
            count = 0
            for p in piles:
                q, r = divmod(p, k)
                count += q + 1 if r else q
                if count > h:
                    return False
            return True

        low = 1
        high = 10**9
        
        while low <= high:
            mid = (low + high) // 2
            if checker(mid):
                high = mid -1
            else:
                low = mid + 1
        return low
        