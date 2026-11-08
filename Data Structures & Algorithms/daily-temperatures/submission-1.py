class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i-prev_idx
            stack.append(i)

        return res