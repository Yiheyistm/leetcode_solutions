class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        room = list(range(n))
        heap = []
        max_meeting_room = [0] * n
        ans = (0, -1) # (room no, no_meeting)
        time = meetings[0][0]

        for s, d in meetings:
            time = max(time, s)
            if not room:
                time = max(time, heap[0][0])

            while heap and time >= heap[0][0]:
                duration, r = heappop(heap)
                heappush(room, r)

            if room:
                r = heappop(room)
                max_meeting_room[r] += 1
                if max_meeting_room[r] > ans[1]:
                    ans = (r, max_meeting_room[r])
                elif max_meeting_room[r] == ans[1] and r <= ans[0]:
                    ans = (r, max_meeting_room[r])
                
                heappush(heap, (time + d - s, r))
        return ans[0]

            



        