class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for word in operations:
            if word[0] == '+' or word[-1] == '+':
                res += 1
            else:
                res -= 1
        return res
        