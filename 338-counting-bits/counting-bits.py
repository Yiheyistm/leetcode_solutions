class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            cnt = 0
            k = i
            while k != 0:
                if k % 2:
                    cnt += 1
                k = k >> 1
            ans.append(cnt)
        return ans


        