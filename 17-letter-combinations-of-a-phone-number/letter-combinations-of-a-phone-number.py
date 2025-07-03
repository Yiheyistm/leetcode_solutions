class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToalph = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        ans = []
        n = len(digits)
        def backtrack(i, stack):
            if len(stack) == n and n >= 1:
                ans.append(''.join(stack))
                return
            
            for j in range(i, n):
                for ch in numToalph[int(digits[j])]:
                    stack.append(ch)
                    backtrack(j + 1, stack)
                    stack.pop()

        backtrack(0,[])
        return ans

        