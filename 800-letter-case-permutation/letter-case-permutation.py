class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        ans = set()

        for i in range(2**n):
            temp = list(s)
            k = 0
            while i:
                if i & 1 and temp[n - k -1].isalpha():
                    temp[n - k -1] = temp[n - k -1].swapcase()
                i >>= 1
                k += 1
            ans.add(''.join(temp))

        return list(ans)

        