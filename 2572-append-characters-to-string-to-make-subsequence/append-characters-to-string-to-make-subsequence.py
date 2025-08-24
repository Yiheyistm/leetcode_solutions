class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        waiting = defaultdict(deque)
        waiting[t[0]].append(iter(t[1:]))
        track = 0
        for ch in s:
            queue = waiting[ch]
            waiting[ch] = deque()
            if queue:
                it = queue.popleft()
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                    track += 1
        
        queue = waiting[t[track]]
        if queue:
            it = queue.pop()
            return len(list(it)) + 1

        return 0
     



        
        