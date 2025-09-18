class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_ = reduce(xor, nums)
        xor_ ^= k
        cnt = 0
        while xor_:
            if xor_ & 1:
                cnt += 1
            xor_ >>= 1
        return cnt
