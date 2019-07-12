class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = [[1]]
        for i in range(1, rowIndex+1):
            list = []
            list.append(1)
            for j in range(1, i):
                list.append(result[i-1][j-1] + result[i-1][j])
            list.append(1)
            result.append(list)
        return result[-1]
