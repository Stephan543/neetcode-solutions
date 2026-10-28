class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtracking Algorithm
        subset = []
        res = set()

        def dfs(total, i):
            if total == target:
                res.add(tuple(subset))
            if total > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(total + candidates[i], i+1)
            subset.pop()
            dfs(total, i+1)
        
        dfs(0,0)
        resres = []
        for i in res:
            resres.append(list(i))
        return resres
        