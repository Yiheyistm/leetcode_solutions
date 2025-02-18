class Solution:
    def numSubarraysWithSum(self, arr: List[int], k: int) -> int:
        bin_dict = {0:1}
        r_sum = 0
        cnt = 0
        for i in range(len(arr)):
            r_sum += arr[i]
            if r_sum - k in bin_dict:
                cnt += bin_dict[r_sum - k]
            if r_sum not in bin_dict:
                bin_dict[r_sum] = 1
            else:
                bin_dict[r_sum] += 1
        return cnt 
        