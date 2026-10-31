class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Decision tree where add L or R bracket
        # Need to check if its valid to add right, based on path, else return

        res = []

        def dfs(path, openedCount, closedCount):
            if openedCount == n and closedCount == n:
                res.append(path)
                return

            if openedCount < n:
                dfs(path + "(", openedCount+1, closedCount)

            if openedCount > closedCount:
                dfs(path + ")", openedCount, closedCount+1)

        dfs("", 0, 0)
        return res