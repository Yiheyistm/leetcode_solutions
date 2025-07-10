class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        if k == 0:
            num_cntr = Counter(nums)
            for k, v in num_cntr.items():
                if v > 1:
                    cnt += 1
        else:            
            seen = set(nums)
            for num in seen:
                if num + k in seen:
                    cnt += 1
        return cnt

        