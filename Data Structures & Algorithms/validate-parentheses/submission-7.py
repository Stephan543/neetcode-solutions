class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False

        stack = []
        brackets ={
            "}":"{",
            "]":"[",
            ")":"("
        }

        for item in s:
            if item in brackets:
                popped = stack.pop()
                if popped != brackets[item]:
                    return False
            else:
                stack.append(item)
        return not stack