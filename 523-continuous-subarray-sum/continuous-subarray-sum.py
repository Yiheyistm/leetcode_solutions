class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        my_dict = defaultdict(int)
        my_dict[0] = -1
        p_sum = 0
        for i in range(len(nums)):
            p_sum += nums[i]
            _, remd = divmod(p_sum, k)
            if remd in my_dict:
                if i - my_dict[remd]  > 1:
                    return True
            else: my_dict[remd] = i
        return False
            
                

        