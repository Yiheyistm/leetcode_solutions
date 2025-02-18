class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remain_dict = {0:1}
        r_sum = 0
        cnt = 0
        for i in range(len(nums)):
            r_sum += nums[i]
            remain = r_sum % k
            if remain in remain_dict:
                cnt += remain_dict[remain]
                remain_dict[remain] += 1
            else:
                remain_dict[remain] = 1
        return cnt

        