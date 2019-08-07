class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        count = 1
        for i in range(1,len(S)):
            if S[i] == S[i-1]:
                count += 1
                if i == len(S)-1 and count >= 3:
                    ans += [[i-count+1, i]]
            else:
                if count >= 3:
                    ans += [[i-count, i-1]]
                count = 1        
        return ans
