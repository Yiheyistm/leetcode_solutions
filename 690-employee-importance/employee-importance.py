"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        def dfs(id):
            nonlocal res
            res += graph[id].importance
            for sub in graph[id].subordinates:
                dfs(sub)

        graph = defaultdict(Employee)
        for emp in employees:
            graph[emp.id] = emp

        dfs(id)
        return res

        