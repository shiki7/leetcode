class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_increasing, is_decreasing = False, False
        for i in range(0, len(A)-1 ):
            if A[i] < A[i+1]:
                is_increasing = True
            if A[i] > A[i+1]:
                is_decreasing = True
        return not (is_increasing and is_decreasing)
