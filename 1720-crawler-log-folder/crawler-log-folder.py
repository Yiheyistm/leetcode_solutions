class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lgStk = []
        for op in logs:
            if op == './': pass
            elif op == '../':
                if lgStk:
                    lgStk.pop()
            else:
                lgStk.append(op)
        return len(lgStk)
        