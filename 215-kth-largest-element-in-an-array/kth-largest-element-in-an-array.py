class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(k, partition):
            if len(partition) == 1:
                return partition[0]
            left, mid, right = [], [], []
            pivot = random.choice(partition)
            for num in partition:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if len(right) >= k:
                return quickSelect(k, right)
            elif len(right) + len(mid) < k:
                return quickSelect(k - (len(right) + len(mid)), left)
            else:
                return pivot

        return quickSelect(k, nums)
            



        