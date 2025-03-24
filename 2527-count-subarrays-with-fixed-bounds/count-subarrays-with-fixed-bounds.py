class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        dec = deque()
        inc = deque()
        left = 0
        invalid = -1
        res = 0
        for i in range(len(nums)):
            while inc and nums[inc[-1]] >= nums[i]:
                inc.pop()
                
            while dec and nums[dec[-1]] <= nums[i]:
                dec.pop()
                
            inc.append(i)
            dec.append(i)
            while dec and inc and (nums[dec[0]] > maxK or nums[inc[0]] < minK):
                invalid = i
                num = nums[left]
                if nums[dec[0]] == num: dec.popleft()
                if nums[inc[0]] == num: inc.popleft()
                left += 1
            if dec and  inc and nums[dec[0]] == maxK and nums[inc[0]] == minK:
                res += max(0, min(dec[0], inc[0]) - invalid)
        return res