class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = dict()

        for i in range(len(matches)):
            winner, looser = matches[i]
            players[looser] = players.get(looser, 0) + 1
            if winner in players and players[winner] != 0:
                players.get(winner, 0) + 1
            else:
                players[winner] = 0
        ans1 = []
        ans2  = []
        
        for key, value in players.items():
            if value == 0:
                ans1.append(key)
            if value == 1:
                ans2.append(key)
        ans1.sort()
        ans2.sort()
        return[ans1, ans2]

        