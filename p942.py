class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        A = list(range(len(S) + 1))
        for char in S:
            if char == "I":
                result.append(A.pop(0))
            elif char == "D":
                result.append(A.pop(-1))
        result.append(A.pop(0))
        return result
