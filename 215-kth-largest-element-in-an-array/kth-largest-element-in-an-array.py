class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        def quickSelect(l, r):
            pvt_val = nums[r]
            l_ptr = l; r_ptr = r
            while l_ptr <= r_ptr:
                while l_ptr <= r_ptr and nums[l_ptr] < pvt_val:
                    l_ptr += 1

                while r_ptr >= l_ptr and nums[r_ptr] > pvt_val:
                    r_ptr -= 1

                if l_ptr <= r_ptr:
                    nums[l_ptr], nums[r_ptr] = nums[r_ptr], nums[l_ptr]
                    r_ptr -= 1
                    l_ptr += 1
            if r_ptr >= target:
                return quickSelect(l, r_ptr)
            elif l_ptr <= target:
                return quickSelect(l_ptr, r)
            else:
                return nums[target]

        return quickSelect(0, n - 1)
            



        