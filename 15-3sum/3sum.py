class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                sm = nums[l] + nums[r]
                if sm == target:
                    if (nums[l - 1] != nums[l]) or (r + 1 >= n or nums[r + 1] != nums[r]):
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sm < target:
                    l += 1
                else:
                    r -= 1

        return res
