class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_dq = deque()
        min_dq = deque()
        left = 0
        count = 0
        
        for right, val in enumerate(nums):
            while max_dq and nums[max_dq[-1]] < val:
                max_dq.pop()
            max_dq.append(right)
            
            while min_dq and nums[min_dq[-1]] > val:
                min_dq.pop()
            min_dq.append(right)
            while nums[max_dq[0]] - nums[min_dq[0]] > 2:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
                    
            count += right - left + 1
        
        return count
