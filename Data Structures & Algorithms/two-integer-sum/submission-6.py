class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = []
        l, r = 0, len(nums)-1
        for i, v in enumerate(nums):
            hm.append((v, i))

        hm.sort()
        while l < r:
            left = hm[l][0]
            right = hm[r][0]
            if (left + right) == target:
                return [min(hm[l][1], hm[r][1]), max(hm[l][1], hm[r][1])]
            elif (left+right) > target :
                r -=1
            else:
                l +=1
        return []