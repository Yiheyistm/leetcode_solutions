class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water_vol = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                btm = stack.pop()
                if not stack:
                    break
                left_idx = stack[-1]
                bound_height = min(height[left_idx], h) - height[btm]
                width = i - left_idx - 1
                water_vol += width * bound_height

            stack.append(i)

        return water_vol

                    


        