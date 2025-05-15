class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        alp = {'a', 'e', 'i', 'o', 'u'}
        xor_pfx = [0]
        for ch in s:
            if ch in alp:
                xor_pfx.append(xor_pfx[-1] ^ ord(ch))
            else:
                xor_pfx.append(xor_pfx[-1])
        pairs = [[xor_pfx[i], i] for i in range(len(xor_pfx))] 
        
        pairs.sort()
        max_ = 0
        i = 0
        while i < len(pairs):
            curr = i
            for j in range(i + 1, len(pairs)):
                if pairs[i][0] ^ pairs[j][0] == 0:
                    max_ = max(max_, pairs[j][1] - pairs[i][1])
                    curr = j
                else:
                    curr = j
                    break
            i = curr if curr != i else i + 1
        return max_
