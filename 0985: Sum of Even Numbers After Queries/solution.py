class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(A)
        for i in range(0, n):
            if i == 0:
                total = 0
                A[queries[i][1]] += queries[i][0] 
                for j in range(n):
                    if A[j] % 2 == 0:
                        total += A[j]
                ans.append(total)                
            else:
                total = ans[i-1]
                if (A[queries[i][1]] + queries[i][0]) % 2 == 0:
                    total += A[queries[i][1]] + queries[i][0]
                if A[queries[i][1]] % 2 == 0:
                    total -= A[queries[i][1]]
                ans.append(total)
                A[queries[i][1]] += queries[i][0]
        return ans
