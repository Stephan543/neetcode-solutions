class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            hm[s].append(i)

        
        return list(hm.values())