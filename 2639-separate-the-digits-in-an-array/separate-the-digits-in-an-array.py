class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separated_list = [int(digit) for num in nums for digit in str(num)]
        return separated_list
        