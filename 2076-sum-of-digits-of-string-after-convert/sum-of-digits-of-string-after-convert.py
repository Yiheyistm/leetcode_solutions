class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        answer = 0
        # convert character into compatible integer
        for char in s:
            str_int = ord(char) - 96
            res += str(str_int)

        # make transform
        for i in range(k):
            ans = sum(int(char) for char in res)
            res = str(ans)
        return ans
        