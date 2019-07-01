class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_brackets = ["(", "{", "["]
        right_brackets = [")", "}", "]"]
        for bracket in s:
            if bracket in left_brackets:
                stack += [bracket]
            elif bracket in right_brackets:
                if stack:
                    if stack[-1] == "(" and bracket == ")" or stack[-1] == "{" and bracket == "}" or stack[-1] == "[" and bracket == "]":
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
