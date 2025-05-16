class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_pfx = [0]
        for ar in arr:
            xor_pfx.append(xor_pfx[-1] ^ ar)

        return [xor_pfx[r + 1] ^ xor_pfx[l] for l, r in queries]
        