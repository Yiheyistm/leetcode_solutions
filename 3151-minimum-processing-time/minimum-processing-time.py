class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        min_time = float('-inf')
        for i in range(len(processorTime)):
            min_time = max(min_time, tasks[ 4 * i] + processorTime[i])
        return min_time
        