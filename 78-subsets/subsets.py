class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(2**n):
            temp = []
            k = 0
            while i > 0:
                if i & 1:
                    temp.append(nums[n - k -1])
                i = i >> 1
                k += 1
            ans.append(temp)
        return ans


        