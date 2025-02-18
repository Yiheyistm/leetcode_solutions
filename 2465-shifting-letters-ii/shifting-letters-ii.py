class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0] * (len(s) + 1)

        for shift in shifts:
            st, end, dir = shift
            temp[st] += 1 if dir == 1 else -1
            temp[end + 1] -= 1 if dir == 1 else -1

        ans = ''
        p_sum = 0
        base = ord('a')
        for t in range(len(s)):
            p_sum += temp[t]
            ans += chr((ord(s[t]) - base + p_sum)% 26 + base)
        return ans


        


        