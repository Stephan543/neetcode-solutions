class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, m = 0, 0, 0
        isSeen = set()

        while j < len(s):
            while s[j] in isSeen:
                isSeen.discard(s[i])
                i +=1
            isSeen.add(s[j])

            m = max(m, j-i + 1)
            j +=1

        return m