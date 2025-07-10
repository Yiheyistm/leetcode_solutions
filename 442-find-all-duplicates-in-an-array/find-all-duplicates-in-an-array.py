class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        ans = []
        for num, freq in num_freq.most_common():
            if freq == 2:
                ans.append(num)
        return ans 