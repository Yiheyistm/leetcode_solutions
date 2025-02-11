class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        while len(arr):
            max_idx = arr.index(max(arr))
            res.append(max_idx + 1)
            res.append(len(arr))
            arr[:max_idx + 1] = arr[max_idx::-1]
            arr = arr[::-1]
            arr.pop()
        return res


        