class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        root = {}
        max_bit_len = max(nums).bit_length()
        for num in nums:
            mask = 1 << (max_bit_len - 1)
            binary = []
            while mask > 0:
                binary.append('1' if mask & num else '0')
                mask >>= 1
  
            curr = root
            for b in binary:
                if b not in curr:
                    curr[b] = {}
                curr = curr[b]
            curr['/'] = 1


        def dfs(num, node, depth, store):
            if depth == max_bit_len: 
                return int(store, 2)

            bit = '1' if (1 << (max_bit_len - 1 - depth)) & num else '0'
            if bit == '0' and '1' in node:
                return dfs(num, node['1'], depth + 1, store + '1')
            elif bit == '1' and '0' in node:
                return dfs(num, node['0'], depth + 1, store + '0')
            else:
                return dfs(num, node[str(bit)], depth + 1, store + str(bit))

        res = 0
        for num in nums:
            res = max(res, num ^ dfs(num, root, 0, ''))
        return res