class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        alpha = {'a':1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        dict_ = defaultdict(int)
        dict_[0] = -1
        temp = 0
        max_diff = 0
        for i, ch in enumerate(s):
            if ch in 'aeiou':
                temp ^= alpha[ch]

            if temp in dict_:
                distance = i - dict_[temp]
                max_diff = max(max_diff, distance)
            else:
                dict_[temp] = i
        return max_diff

