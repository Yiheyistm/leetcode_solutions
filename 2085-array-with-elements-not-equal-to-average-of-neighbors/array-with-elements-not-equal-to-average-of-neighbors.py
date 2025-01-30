class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        median = len(nums) // 2
        i = 0
        j = len(nums) -1
        while i<j:
          ans.append(nums[i])
          ans.append(nums[j])
          i += 1
          j -= 1
        if len(nums) % 2 == 1:
            ans.append(nums[i])
        return ans
        