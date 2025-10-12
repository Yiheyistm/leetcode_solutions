class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = defaultdict(list) # used to keep update the task
        self.priority_tasks = [] # to identify the priority tasks among the users

        for task in tasks:
            userId, tId, pr = task
            self.tasks[tId] = [userId, pr]
            heappush(self.priority_tasks, (-pr, -tId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = [userId, priority]
        heappush(self.priority_tasks, (-priority, -taskId, userId))      

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.tasks[taskId]
        self.tasks[taskId] = [userId, newPriority]
        heappush(self.priority_tasks, (-newPriority, -taskId, userId))    
        
    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]     

    def execTop(self) -> int:
        if self.priority_tasks:
            while self.priority_tasks:
                p, t, u = heappop(self.priority_tasks)
                if -t in self.tasks:
                    uId, pr = self.tasks[-t]
                    if uId == u and pr == -p:
                        self.rmv(-t)
                        return uId
        return -1        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()