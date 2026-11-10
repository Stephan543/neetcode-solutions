class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count =0
        for word in words:
            for i, v in enumerate(pref):
                if word[i] != v:
                    break
            else:
                count +=1
        return count