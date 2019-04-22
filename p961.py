class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dict = {}
        for node in A:
            if node in dict.keys():
                dict[node] += 1
            else:
                dict[node] = 1
        return max(dict, key=dict.get)
