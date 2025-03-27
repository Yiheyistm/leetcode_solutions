class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def checker(ln):
            pfx = [0] * (len(nums) + 1)
            for i in range(ln):
                l, r , val = queries[i]
                pfx[l] += val
                pfx[r + 1] -= val
            for v in range(1, len(pfx)):
                pfx[v] = pfx[v] + pfx[v-1]

            for i in range(len(nums)):
                if pfx[i] < nums[i]:
                    return False
            return True
        
        if not checker(len(queries)):
            return -1
        low = -1
        high = len(queries)
        while low + 1 < high:
            mid = (low + high) // 2
            if checker(mid):
                high = mid
            else:
                low = mid

        return high
        