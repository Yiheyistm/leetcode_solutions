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

        distance = defaultdict(list)
        for val, i in pairs:
            distance[val].append(i)

        max_diff = 0
        for lst in distance.values():
            max_diff = max(max_diff, max(lst) - min(lst))
  
        return max_diff
