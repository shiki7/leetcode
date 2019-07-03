class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            list = []
            list.append(1)
            for j in range(1, i):
                list.append(result[i-1][j-1] + result[i-1][j])
            list.append(1)
            result.append(list)
        return result
