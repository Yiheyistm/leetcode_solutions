class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        temp = [0] * (len(nums) + 1)
        for req in requests: #LINE SWEEP ALGORITHMS
            st, end = req
            temp[st] += 1
            temp[end + 1] -= 1

        pfx_sum = [0] * len(temp)
        for i in range(len(temp)): # FIND PREFIX SUM FROM TEMP
            pfx_sum[i] = (pfx_sum[i - 1] + temp[i])

        mx_sum = 0
        pfx_sum.sort(reverse= True)
        MOD = 10**9 + 7
        for i, n in enumerate(nums): # MULTIPLING MOST FREQUENT ELEMENT WITH LARGE NUMBER IN THE LIST
            mx_sum += ((pfx_sum[i] * n))
        return mx_sum % MOD


        

        