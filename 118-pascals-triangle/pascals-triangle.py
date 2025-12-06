class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            temp = [1]
            if ans:
                for j in range(1, len(ans[-1])):
                    last = ans[-1]
                    temp.append(last[j] + last[j-1])
                temp.append(1)
            ans.append(temp)
        return ans
        