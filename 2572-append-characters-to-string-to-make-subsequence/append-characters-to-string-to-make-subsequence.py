class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        dq = deque(list(t))
        for ch in s:
            if dq and ch == dq[0]:
                dq.popleft()
        return len(dq)
     



        
        