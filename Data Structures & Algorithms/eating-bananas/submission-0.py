class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)

        def countHours(k):
            t = 0
            for i in piles:
                t +=  math.ceil(i/k)
            return t

        while minK < maxK:
            currK = (minK + maxK) // 2
            t = countHours(currK)

            if t > h:
                minK = currK + 1
            else:
                maxK = currK

        
        return minK