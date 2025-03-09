class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=[0]*len(deck)
        q= list(range(len(deck)))
        i = 0
        s = 0
        while i < len(deck):
            if s < len(q) -1:
                rem = q[s + 1]
                q.append(rem)
            res[q[s]] = deck[i]
            s += 2
            i += 1
        return res
