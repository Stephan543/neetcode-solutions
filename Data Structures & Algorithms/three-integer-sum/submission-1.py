class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                compliment = (-nums[i] - nums[j])
                if compliment in seen:
                    res.add(tuple((sorted((nums[i], nums[j], compliment)))))
                seen.add(nums[j])
        fr = []
        for x in res:
            fr.append(x)
        return fr