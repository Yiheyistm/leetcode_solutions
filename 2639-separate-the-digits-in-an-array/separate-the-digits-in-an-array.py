class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separated_list = []
        for num in nums:
            for digit in str(num):
                separated_list.append(int(digit))
        return separated_list
        