class Solution:
    def reachNumber(self, target: int) -> int:
        # since the moves are symmetry the minimum move for -ve target == +ve target
        # which mean we can move to the right until current number S(k) greater than or equals to target but when surpass the target we have to make our move back to left let say current steps are i so we go left by 2*i value with repeatation of this steps finally it will be S(k) - 2 *(x) = target, s(k) - target = 2 * x
        t = abs(target)
        k = 0 
        sk = 0 # S(k)
        while sk < t or (sk - t) % 2 == 1:
            k += 1
            sk += k # can use sk = (k * (k + 1) / 2) instead
        return k