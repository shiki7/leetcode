class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        
        for i in range(len(A) - 1, 1, -1):
            a, b, c = A[i-2:i+1]
            if a + b > c:
                return a + b + c
            
        return 0
