class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                side = nums[i] + nums[j]
                low = j
                high = len(nums)
                while low + 1 < high:
                    mid = (high + low) // 2
                    if nums[mid] >= side:
                        high = mid
                    else:
                        low = mid
                cnt += (low - j)
        return cnt
        