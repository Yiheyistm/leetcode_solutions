class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        upperBound = 2**31 -1
        lowerBound = -(2 ** 31)
        isNeg = False
        s = s.strip()
        i = 0
        while i < len(s):
            if s[i].isdigit():
                break
            elif (s[i] == '-' or s[i] == '+') and i == 0:
                isNeg = True if s[i] == '-' else False
            else:
                return 0
            i += 1

        if i >= len(s):
            return 0

        s = s[i:]
        j = 0
        while j < len(s):
            if not s[j].isdigit():
                break
            j += 1

        s = s[:j]
        num = int(s) * (-1 if isNeg else 1)
        if num > upperBound:
            return upperBound
        if num < lowerBound:
            return lowerBound
        return num

            
        