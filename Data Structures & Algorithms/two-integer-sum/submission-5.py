class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = []
        l, r = 0, len(nums)-1
        for i, v in enumerate(nums):
            hm.append((i, v))

        hm.sort()
        while l < r:
            left = hm[l][1]
            right = hm[r][1]
            if (left + right) == target:
                return [min(hm[l][0], hm[r][0]), max(hm[l][0], hm[r][0])]
            elif (left+right) > target :
                r -=1
            else:
                l +=1
        return []