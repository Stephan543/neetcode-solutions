class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return [l,r]
            elif total > target:
                r -= 1
            else:
                l += 1
        return [0,0]