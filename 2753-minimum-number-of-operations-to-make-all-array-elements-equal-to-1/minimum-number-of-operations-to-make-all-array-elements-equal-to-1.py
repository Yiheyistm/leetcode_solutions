class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)

        min_op = inf
        for i in range(n):
            prev = nums[i]
            cnt = 0
            for j in range(i + 1, n):
                prev = gcd(prev, nums[j])
                if prev == 1:
                    min_op = min(min_op, cnt + n - counter[1])
                    break
                cnt += 1
        return min_op if min_op != inf else -1


