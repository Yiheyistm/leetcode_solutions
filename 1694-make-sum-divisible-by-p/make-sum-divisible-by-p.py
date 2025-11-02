class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # To make the array divisible by p we have to remove sub_arraysum(prfx[j] - prfx[i]) % p == rem
        # by rearranging prfx[i] % p == (prfx[j] - rem + p) % p
        pfx = list(accumulate(nums))
        rem = pfx[-1] % p

        if rem == 0:
            return 0

        di = {0: -1}
        min_sub = inf
        for r in range(len(pfx)):
            mod = pfx[r] % p
            needed = (mod - rem + p) % p
            if needed in di:
                    min_sub =min(min_sub, r - di[needed])
            di[mod] = r
            
        return min_sub if min_sub < len(nums) else -1
