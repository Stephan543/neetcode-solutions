class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        
        longest = 1
        localLongest = 1
        i, j = 0,1
        isSeen = set(s[i])

        while j < len(s):
            if s[j] in isSeen:
                isSeen.clear()
                i+=1
                j=i+1
                isSeen.add(s[i])
                localLongest = 1
            else:
                isSeen.add(s[j])
                localLongest +=1
                j+=1
            longest = max(longest,localLongest)
        return longest
