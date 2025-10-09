class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water_vol = 0
        for i in range(len(height)):
            mn_idx = i
            while stack and stack[-1][1] <= height[i]:
                pop_idx, val = stack.pop()
                
                if stack and stack[-1][1] > val:
                    water_vol += (i - pop_idx) * (min(stack[-1][1], height[i]) - val)
                mn_idx = pop_idx
            stack.append((mn_idx, height[i]))
            
        return water_vol

                    


        