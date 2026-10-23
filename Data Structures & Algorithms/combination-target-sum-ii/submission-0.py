class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        subset = []

        def dfs(total, i):
            if total == target:
                res.add(tuple(subset))
                return
            if total > target or i >= len(candidates):
                return
       
            
            subset.append(candidates[i])
            dfs(total + candidates[i], i+1)
            subset.pop()
            dfs(total, i+1)
        
        dfs(0, 0)
        return [list(t) for t in res]

