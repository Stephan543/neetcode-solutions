import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha_map = {char: 0 for char in string.ascii_uppercase}
        l, r, res = 0, 0 ,0


        def isValid(window_size: int, hf: int, k: int) -> bool:
            if window_size-hf <= k:
                return True
            return False
        
        def mostFrequentCount(alpha_map: dict[str,int]) -> int:
            m = 0
            for v in alpha_map.values():
                m = max(m,v)
            return m

        while r < len(s):
            window_size = r-l+1
            alpha_map[s[r]] += 1
            hf = mostFrequentCount(alpha_map)
            if not isValid(window_size, hf, k):
                alpha_map[s[l]] -=1
                l +=1   
            else:
                res = max(window_size, res)
            r +=1                      


       

        return res 