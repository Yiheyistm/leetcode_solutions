class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = {}
        i = 0
        while i < len(nums):
            cp = nums[i] - 1
            if nums[i] != nums[cp] and nums[i] in res:
                res.pop(nums[i])
            if cp == i: i += 1
            else:
                if nums[i] == nums[cp]:
                    res[i +  1] = 1
                    i += 1
                else:
                    nums[cp], nums[i] = nums[i], nums[cp]

        return list(res.keys())
        