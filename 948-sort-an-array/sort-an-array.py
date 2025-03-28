class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l_arr, r_arr):
            l, r = 0, 0
            merged = []
            while l < len(l_arr) and r < len(r_arr):
                if l_arr and r_arr and l_arr[l] <= r_arr[r]:
                    merged.append(l_arr[l])
                    l += 1
                elif l_arr and r_arr and l_arr[l] > r_arr[r]:
                    merged.append(r_arr[r])
                    r += 1
            while l < len(l_arr):
                merged.append(l_arr[l])
                l += 1
            while r < len(r_arr):
                merged.append(r_arr[r])
                r += 1
            return merged

        def merge_sort(left, right, arr):
            if right == left:
                return [arr[left]]
            mid = (left + right) // 2
            return merge(merge_sort(left, mid, arr), merge_sort(mid + 1, right, arr))
        return merge_sort(0, len(nums) - 1, nums)
        