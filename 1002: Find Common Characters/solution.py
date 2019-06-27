class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        keyword = A[0]
        answer = []
        for char in keyword:
            counter = 0
            for word in A:
                if char in word:
                    counter += 1
            if counter == len(A):
                answer += [char]
                # 一致した値は削除しておく
                for i in range(len(A)):
                    A[i] = A[i].replace(char, "", 1)
                    
        return answer
