class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index_dict = {char: i for i, char in enumerate(S)}
        
        j = anchor = 0
        ans = []
        for i, char in enumerate(S):
            j = max(j, last_index_dict[char])
            if i == j:
                ans += [i - anchor + 1]
                anchor = i + 1
        return ans
