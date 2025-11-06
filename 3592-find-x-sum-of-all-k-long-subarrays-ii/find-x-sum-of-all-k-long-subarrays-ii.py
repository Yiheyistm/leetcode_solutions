class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        '''
        Let's try to add new nums on the topX and pop the smallest one and add it to the remain after update its freq
        and when remove element also check if the num is in topx and if any change is happen make sure to update the both topx and remain
        since we always try to add the num on the topX so we have to make sure the lenght of the topX not greater than x value (balance)
        also update the curr_sum through the process

        '''
        topX = SortedList() # (freq, val)
        remain = SortedList() # (freq, val)
        freq = defaultdict(int) # val -> freq
        curr_sum = 0

        def balance():
            nonlocal curr_sum
            if len(topX) > x:
                f, n = topX.pop(0) # since it is BST it costs only log(n)
                curr_sum -= f * n
                remain.add((f, n))

            if len(topX) < x and remain:
                f, n = remain.pop() # remove the largest
                topX.add((f, n))
                curr_sum += f * n

            if topX and remain and topX[0] < remain[-1]:
                f1, n1 = topX.pop(0)
                f2, n2 = remain.pop()
                topX.add((f2, n2))
                remain.add((f1, n1))
                curr_sum += (f2*n2 - f1*n1)


        def add(num):
            nonlocal curr_sum
            if num in freq: # if num found the freq we have to be remove wherever it found inorder to update it
                if (freq[num], num) in topX: # look up on sorted list costs log(n)
                    topX.remove((freq[num], num))
                    curr_sum -= (freq[num] * num) # since we remove num we have to be remove it from the sum also
                else:
                    remain.remove((freq[num], num))

            freq[num] += 1
            topX.add((freq[num], num)) # always try to add it on the topX 
            curr_sum += (freq[num] * num)
            balance() # check if the topX is off by one element

        def remove(num):
            nonlocal curr_sum
            if num in freq: # if num found the freq we have to be remove wherever it found inorder to update it
                if (freq[num], num) in topX: # look up on sorted list costs log(n)
                    topX.remove((freq[num], num))
                    curr_sum -= (freq[num] * num) # since we remove num we have to be remove it from the sum also
                else:
                    remain.remove((freq[num], num))

            freq[num] -= 1
            topX.add((freq[num], num)) # always try to add it on the topX 
            curr_sum += (freq[num] * num)
            balance() # check if the topX is off by one element

        res = []
        for i in range(k): # process the first k elements
            add(nums[i])
        
        res.append(curr_sum)

        for i in range(k, len(nums)): # process the rest
            remove(nums[i - k])
            add(nums[i])
            res.append(curr_sum)
        
        return res