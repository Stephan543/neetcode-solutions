class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        localLongest = 1
        i, j = 0,1
        isSeen = set(s[i])

        while j < len(s):
            if s[j] in isSeen:
                localLongest = 1
                isSeen.clear()
                isSeen.add(s[j])
                i=j
                j=j+1
            else:
                isSeen.add(s[j])
                localLongest +=1
                j+=1
            longest = max(longest,localLongest)
        return longest
