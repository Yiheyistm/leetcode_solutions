class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ''' this is the math to calculate the absolute differece from prefix and suffix sum e.g [2,3,5]
        pfx = 0 2,5,10 exclusive sum
        sfx = 10, 8, 5 ,0
        therefore for i = 1 i.e 3
        there are i numbers less than 3 and n - k -1(3-1-1 = 1) greater than 3 which means 2 and 5 respectively. - 1 indicate that exclude the num itself
        so to find the differnce i*3 - pfx[i -1] for the left side and sfx[i+1] - (n - k - 1) * 3
        '''
        n = len(nums)
        ans = []
        pfx = 0
        sfx = sum(nums)
        for k in range(n):
            sfx -= nums[k]
            l = k*nums[k] - pfx
            r = sfx - (n - k - 1)*nums[k]
            pfx += nums[k]
            ans.append(l + r)
        return ans

    
        