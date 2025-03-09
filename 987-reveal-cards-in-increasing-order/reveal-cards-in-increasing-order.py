class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque()
        n = len(deck)
        for i in range(n-1, -1 ,-1):
            if dq:
                f = dq.pop()
                dq.appendleft(f)
            dq.appendleft(deck[i])
        return list(dq)