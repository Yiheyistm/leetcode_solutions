
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        waiting = defaultdict(deque)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        count = 0
        
        for ch in s:
            queue = waiting[ch]
            waiting[ch] = deque()

            while queue:
                it = queue.popleft()
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    count += 1
        
        return count
