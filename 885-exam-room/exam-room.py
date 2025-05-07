class ExamRoom:

    def __init__(self, n: int):
        self.size = n
        self.max_heap = [(-n , 0, n - 1)]
        self.interval = {(0, n - 1)}

        

    def seat(self) -> int:
        while self.max_heap:
            dist,start, end = heappop(self.max_heap)

            if (start, end) not in self.interval: continue

            self.interval.remove((start, end))
            if start == 0:
                seat = 0
            elif end == self.size - 1:
                seat = end
            else:
                seat = (start + end) // 2
            
            if seat - 1 >= start:
                dist = (seat - 1 - start) // 2 if start != 0 else seat - start
                heappush(self.max_heap, (-dist, start, seat - 1))
                self.interval.add((start, seat - 1))
            if seat + 1 <= end:
                dist = (end - (seat + 1)) // 2 if end != self.size - 1 else end - (seat + 1)
                heappush(self.max_heap, (-dist, seat + 1, end))
                self.interval.add((seat + 1, end))
            return seat
                
        
    def leave(self, p: int) -> None:
        left = p - 1
        right = p + 1

        left_interval = None
        right_interval = None
        for start, end in self.interval:
            if end == left:
                left_interval = (start, end)
            if start == right:
                right_interval = (start, end)
        if left_interval:
            self.interval.remove(left_interval)
            
        if right_interval:
            self.interval.remove(right_interval)

        nw_start = left_interval[0] if left_interval else p
        nw_end = right_interval[1] if right_interval else p
        
        self.interval.add((nw_start, nw_end))
        heappush(self.max_heap, (-(nw_end - nw_start), nw_start, nw_end))
        

        
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)