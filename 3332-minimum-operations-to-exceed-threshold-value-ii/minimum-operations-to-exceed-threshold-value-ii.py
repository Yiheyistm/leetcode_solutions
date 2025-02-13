class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        op = 0
        while len(nums) >= 2:
            mn1 = heappop(nums)
            mn2 = heappop(nums)
       
            if mn1 >= k: break
            
            prod = (2 * mn1) + mn2
            heappush(nums, prod)
            op += 1
        return op

        