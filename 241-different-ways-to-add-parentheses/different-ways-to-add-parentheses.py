class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(exp):
            if exp.isdigit():
                return [int(exp)]
            result = []
            for i, ch in enumerate(exp):
                if ch in "+-*":
                    left_exp = exp[:i]
                    right_exp = exp[i+1:]

                    left_result = dfs(left_exp)
                    right_result = dfs(right_exp)
                    for l_val in left_result:
                        for r_val in right_result:
                            if ch == "+":
                                result.append(l_val + r_val)
                            if ch == "-":
                                result.append(l_val - r_val)
                            if ch == "*":
                                result.append(l_val * r_val)
            return result
        return dfs(expression)

            
        