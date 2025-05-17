class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        freq = { 0: -1}      
        cnt = 0
        for i in range(len(arr)):
            xor = 0
            for j in range(i + 1, len(arr)):
                xor ^= arr[j]
                if xor == arr[i]:
                    cnt += j - i
        return cnt
        
        