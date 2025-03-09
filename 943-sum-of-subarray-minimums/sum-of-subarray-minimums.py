class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sm = 0
        stk = []
        no_sub = 0
        MOD = 10 ** 9 + 7
        for i in range(len(arr)):
            # Monotonic Increasing stack
            while stk and stk[-1][0] > arr[i]:
                val, idx = stk.pop()
                left = idx - (stk[-1][1] if stk else -1) # Distace to previous smaller
                right = i - idx # Distace to next smaller
                sm = (sm + (val * left * right)) % MOD
            stk.append((arr[i], i))
        
        # Process the remainig stack
        while stk:
            val, idx = stk.pop()
            left = idx - (stk[-1][1] if stk else -1) # Distace to previous smaller
            right = len(arr) - idx # Distance to the end of the arry
            sm = (sm + (val * left * right)) % MOD
        return sm
            