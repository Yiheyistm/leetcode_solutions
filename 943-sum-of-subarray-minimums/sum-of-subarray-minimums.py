class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(float('-inf')) # Since i use monotonic stack float('-inf') helps to pop all element from the stack
        sm = 0
        stk = []
        no_sub = 0
        MOD = 10 ** 9 + 7
        for i in range(len(arr)):
            # Monotonic Increasing stack
            while stk and arr[stk[-1]] > arr[i]:
                idx = stk.pop()
                left = idx - (stk[-1] if stk else -1) # Distace to previous smaller
                right = i - idx # Distace to next smaller
                sm = (sm + (arr[idx] * left * right)) % MOD
            stk.append(i)
        return sm
            