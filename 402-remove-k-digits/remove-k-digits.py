class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        stack = stack[:len(stack) - k]
        ans = ''.join(stack)
        return ans.lstrip('0') or '0'

        