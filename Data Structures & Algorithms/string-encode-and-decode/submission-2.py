class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res+=str(len(item))+"#"+item
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        count =0
        i=0
        while i < len(s):
            j=i
            while s[j] != "#":
                j +=1
            count = int(s[i:j])
            j+=1
            res.append(s[j:j+count])
            i += j + count
        return res

            
