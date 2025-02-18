class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        return max(tasks[ 4 * i] + processorTime[i] for i in range(len(processorTime)))
        