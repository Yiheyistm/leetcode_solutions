class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for val in nums:
            if val in seen:
                ans ^= val
            seen.add(val)
        return ans

        