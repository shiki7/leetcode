class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = S
        for i in range(0, len(S)-1):
            before_result = result
            for j in range(0, len(result)-1):
                if result[j] == result[j+1]:
                    result = result.replace(result[j]+result[j+1], '00')
            result = result.replace('0', '')
            if before_result == result:
                return result
