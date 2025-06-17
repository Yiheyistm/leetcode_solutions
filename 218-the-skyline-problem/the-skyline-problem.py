class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))  
            events.append((right, 0, 0))           

        events.sort()
        
        heap = [(0, float('inf'))]
        result = [[0, 0]]

        for x, neg_h, r in events:
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))
            else:
                while heap and heap[0][1] <= x:
                    heapq.heappop(heap)
            
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            current_height = -heap[0][0]

            if result[-1][1] != current_height:
                result.append([x, current_height])

        return result[1:]