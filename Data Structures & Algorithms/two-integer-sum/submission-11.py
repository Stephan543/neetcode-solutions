class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, v in enumerate(nums):
            hm[v] =i

        for i, v in enumerate(nums):
            res = target - v
            if res in hm and hm[res] != i:
                return [min(hm[res], i), max(hm[res],i)]