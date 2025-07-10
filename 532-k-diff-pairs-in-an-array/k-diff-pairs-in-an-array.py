class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        def checker(num, i):
            nonlocal k
            l = i
            h = len(nums)
            while l + 1 < h:
                mid = (l + h) // 2
                if abs(num - nums[mid]) == k and (num, nums[mid]) not in pairs:
                    pairs.add((num, nums[mid]))
                    return
                elif abs(num - nums[mid]) == k and (num, nums[mid]) in pairs:
                    return
                elif abs(num - nums[mid]) > k: h = mid
                else: l = mid
            
        nums.sort()   
        pairs = set()
        for i in range(len(nums)):
            checker(nums[i], i)
        return len(pairs)

        