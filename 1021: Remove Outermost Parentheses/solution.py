class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        check = 0
        for char in S:
            if char == '(':
                check += 1
                if check > 1:
                    ans += "("
            if char == ')':
                check -= 1
                if check > 0:
                    ans += ")"
        return ans
