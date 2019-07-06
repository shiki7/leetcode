class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A_str = ""
        result = []
        for i in A:
            A_str += str(i)
        sum = int(A_str) + K
        for i in str(sum):
            result += [int(i)] 
        return result
