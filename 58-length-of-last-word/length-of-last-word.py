class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = ''
        s = s[::-1]
        for i in s:
            if i == " " and len(ans)>0:
                return len(ans)
            if i == " ":
                continue
            ans += i
        return len(ans)

        