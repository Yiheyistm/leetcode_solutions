class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(s):
            vist.add(s)
            for neigh in rooms[s]:
                if neigh not in vist:
                    dfs(neigh)
        vist = set()
        dfs(0)
        return len(vist) == len(rooms)
        