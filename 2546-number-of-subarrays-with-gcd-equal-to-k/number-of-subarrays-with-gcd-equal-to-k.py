class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] % k: continue
            r_gcd = 0
            for j in range(i, len(nums)):
                r_gcd = gcd(r_gcd, nums[j])
                if r_gcd  == k:
                    ans += 1
                if r_gcd < k: break
        return ans
        