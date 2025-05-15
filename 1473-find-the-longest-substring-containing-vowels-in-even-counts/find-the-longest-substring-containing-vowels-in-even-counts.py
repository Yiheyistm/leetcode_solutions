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
        l = 0
        diff = False
        for r in range(1, len(pairs)):
            diff = False
            if pairs[r][0] ^ pairs[l][0] != 0:
                max_ = max(max_, pairs[r - 1][1] - pairs[l][1])
                diff = True
                l = r
            
        if not diff:
            max_ = max(max_, pairs[-1][1] - pairs[l][1])

        return max_ if xor_pfx[-1] else len(s)
