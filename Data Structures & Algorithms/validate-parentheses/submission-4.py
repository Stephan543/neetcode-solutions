class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False

        stack = []
        brackets ={
            "{":"}",
            "[":"]",
            "(":")"
        }

        for item in s:
            if item in brackets:
                stack.append(item)
            else:
                if not stack:
                    return False

                popped = stack.pop()
                if brackets[popped] != item:
                    return False
            if len(stack)!=0:
                return False
        return True

