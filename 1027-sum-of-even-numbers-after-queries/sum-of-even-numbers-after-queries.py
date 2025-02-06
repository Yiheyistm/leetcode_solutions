class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_sum = sum(x for x in nums if x % 2 == 0)
        for i in range(len(queries)):
            val, idx = queries[i]
            new_sum = nums[idx] + val
            if new_sum % 2 == 0 and nums[idx] % 2 == 0:
                even_sum  += val
            elif new_sum % 2 == 0 and nums[idx] % 2 != 0:
                even_sum  += new_sum
            elif new_sum % 2 != 0 and nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] = new_sum
            ans.append(even_sum)
            even_sum = ans[i]
        return ans
        