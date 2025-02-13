class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l, r = 0, 0
        mx_len = 0
        win_size = 0
        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                mx_len = max(r - l + 1, mx_len)
                r += 1
            else:
                st.remove(s[l])
                l += 1
            
        return mx_len
        