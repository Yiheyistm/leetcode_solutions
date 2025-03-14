class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        1. We can find the largest are by visting the next element until finding the smallest element so far
        2. for this purpose we can use min monotonic stack(increasing)
        3. and find the largest area every time we pop
        4. The stack might not empty at the end of the loop so we have to be calculate the area 
        or append 0 at the end of the height because 0 can pop every element on the monotonic increasing stack and have no effect on the max area
        '''
        stack = []
        mx_area = 0
        heights.append(0)
        for i, val in enumerate(heights):
            nwIdx = i
            while stack and stack[-1][1] >= val:
                idx, v = stack.pop()
                temp_area = (i - idx) * v
                mx_area = max(mx_area, temp_area)
                nwIdx = idx
            stack.append((nwIdx, val))
        return mx_area


        