class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hf = {}
        for item in nums:
            if item not in hf:
                hf[item] = 1
            else:
                hf[item] +=1
        
        # create a sorted array based on hf
        sorted_keys_asc = sorted(hf, key=hf.get, reverse=True)
        return sorted_keys_asc[:k]