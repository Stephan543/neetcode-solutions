class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, remainingNums):
            if len(remainingNums) == 0:
                res.append(path.copy())
                return 
            for i in range(len(remainingNums)):
                path.append(remainingNums[i])
                dfs(path, remainingNums[:i]+ remainingNums[i+1:])
                path.pop()

        dfs([], nums)
        return res