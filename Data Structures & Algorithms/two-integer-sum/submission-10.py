class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, v in enumerate(nums):
            hm[v] =i

        for v in hm:
            res = target - v
            if res in hm and hm[res] != hm[v] :
                
                return [min(hm[res], hm[v]), max(hm[res], hm[v])]