class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def checker(mid):
            ball = 1
            st = position[0]
            for i in range(1, len(position)):
                if position[i] - st >= mid:
                    st = position[i]
                    ball += 1
                    
            return ball >= m

        low = 1
        high = position[-1] - position[0]
        ans = -1
        while low  <= high:
            mid = (low + high) // 2
            if checker(mid):
                low = mid + 1
                ans = mid
            else: 
                high = mid - 1

        return  ans
        