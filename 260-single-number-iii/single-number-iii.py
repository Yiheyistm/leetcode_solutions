class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_ = 0
        for num in nums:
            xor_ ^= num

        diff_bit = xor_ & -xor_ #this gives the LSB in the right
        a, b, = 0, 0
        for num in nums:
            if diff_bit & num:
                a ^= num
            else:
                b ^= num
        return [a, b]




        