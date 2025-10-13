class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_char = set()
        longest = 0
        l = 0
        for r, ch in enumerate(s):
            if ch in prev_char:
                while ch in prev_char:
                    prev_char.remove(s[l])
                    l += 1
            prev_char.add(ch)
            longest = max(longest, r - l + 1)
        return longest

        