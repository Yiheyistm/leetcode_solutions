class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        zero_count = 0
        for r in range(len(s) - 1, -1, -1):
            if s[r] == '0':
                zero_count += 1
            elif s[r] == '1':
                steps += zero_count

        return steps

        