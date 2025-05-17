class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            k = 0
            n = num if num >= 0 else num + (1 << 32) # 32 bit simulation for -ve nums like -4 to 1...11100
            while n > 0:
                if n & 1:
                    freq[k] += 1
                n >>= 1
                k += 1
        ans = [0] * 32
        for key, val in freq.items():
            if val % 3:
                ans[key] = 1

        res = 0
        for bit in reversed(ans):
            res = (res << 1) | bit

        if ans[31] == 1: # if the 31th bit is still 1 i.e negative num so we have to back it to previous negative decimal
            res -= (1 << 32)
        return res

        