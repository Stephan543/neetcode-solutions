class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        def dfs(i, path):
            if i == len(nums):
                res.add(tuple(path))
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)

        dfs(0, [])
        resList = []
        for i in res:
            resList.append(list(i))

        return resList