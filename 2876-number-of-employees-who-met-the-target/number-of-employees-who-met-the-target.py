class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        l, h = -1, len(hours)
        while l + 1 < h:
            mid = (l + h) // 2
            if hours[mid] >= target: h = mid
            else: l = mid
        return len(hours) - h
        