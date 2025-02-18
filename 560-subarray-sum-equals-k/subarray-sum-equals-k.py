class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = r = 0
        sm = 0
        my_dict = {0: 1}
        cnt = 0
        for r in range(len(nums)):
            sm += nums[r] 
            if sm - k in my_dict:
                cnt += my_dict[sm - k]
            if sm not in my_dict:
                my_dict[sm] = 1
            else:
                my_dict[sm] += 1
        return cnt



        