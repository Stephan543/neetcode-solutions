class Solution:
    def isValid(self, s: str) -> bool:
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
                popped = stack.pop()
                if brackets[popped] != item:
                    return False
        return True

