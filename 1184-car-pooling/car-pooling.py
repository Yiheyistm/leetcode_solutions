class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        line_sweep = [0] * 10001
        for passanger, start, end in trips:
            line_sweep[start] += passanger
            line_sweep[end] -= passanger
        route = [0]
        for i, line in enumerate(line_sweep, start = 1):
            route.append(route[i - 1] + line)
            if route[i] > capacity:
                return False
        return True

        
        