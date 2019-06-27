class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for char in S:
            if char == "(":
                stack += ["("]
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack += [")"]
        return len(stack)
