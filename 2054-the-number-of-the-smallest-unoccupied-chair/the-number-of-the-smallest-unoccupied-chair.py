class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        frds = [(a, d, i) for i, [a, d] in enumerate(times)]
        frds.sort()
        heap = []
        seat = list(range(len(times)))
        for a ,d, i in frds:
            while heap and a >= heap[0][0]:
                _, s = heappop(heap)
                heappush(seat , s)
               
            x = heappop(seat)
                
            if i == targetFriend:
                return x
            
            heappush(heap, (d, x))
          
        # target = times[targetFriend]
        # arr = []
        # for i in range(len(times)):
        #     arr.append(i)
        # times.sort()
        # prev = times[0][1]
        # ind = times.index(target)
        # for i in range(1,len(times)):
        #     x , y = times[i]
        #     if x <= prev :
        #         arr[i] = arr[i-1]
        #     prev = y
        # print(arr)
        # return arr[ind]
        
                