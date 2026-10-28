class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtracking Algorithm
        res = []
        candidates.sort()

        def dfs(total, path, idx ):
            if total == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(total + candidates[i], path, i+1)
                path.pop()
        
        dfs(0,[], 0)
        return res
        