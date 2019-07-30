class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        val = 0
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3, n+1):
            val = a+b+c
            a = b
            b = c
            c = val
        return val
