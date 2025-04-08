class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def checker(mid):
            j = 0
            for h in houses:
                if abs(heaters[j] - h) > mid:
                    while j < len(heaters) and abs(heaters[j] - h) > mid:
                        j += 1
                    if j == len(heaters):
                        return False
            return True

        l = -1; h = 10**9
        while l + 1 < h:
            mid = (l + h) // 2
            if checker(mid):
                h = mid
            else:
                l = mid
        return h

        