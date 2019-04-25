class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares = []
        for number in A:
            squares.append(pow(number, 2))
        return sorted(squares)
