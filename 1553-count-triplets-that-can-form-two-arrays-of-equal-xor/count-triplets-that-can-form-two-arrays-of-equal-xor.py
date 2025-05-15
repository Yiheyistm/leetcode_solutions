class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor_pfx = [0]
        for num in arr:
            xor_pfx.append(xor_pfx[-1] ^ num)
        
        subarray = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                subarray.append((i, j))
        
        ans = 0
        for i, k in subarray:
            if xor_pfx[k + 1] ^ xor_pfx[i] == 0:
                ans += k - i
        return ans
        