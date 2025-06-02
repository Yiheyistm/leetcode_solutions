class Solution:
    def largestInteger(self, num: int) -> int:
        nums_str = list(str(num))
        odd_heap = []
        even_heap = []
        for num in nums_str:
            if int(num) % 2:
                heappush(odd_heap, -int(num))
            else:
                heappush(even_heap, -int(num))
        ans = ''
        for num in nums_str:
            val = heappop(odd_heap) if int(num) %2 else heappop(even_heap)
            ans += str(-val)
        return int(ans)

        