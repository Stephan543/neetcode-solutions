class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = 0
        res = []
        for i in range(0, len(temperatures)):
            if i == len(temperatures)-1:
                res.append(0)
                return res
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
            else:
                res.append(0)
        return res