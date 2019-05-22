class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = []
        for x in ops:
            if x == "C":
                result.pop()
            elif x == "D":
                result.append(int(result[-1])*2)
            elif x == "+":
                result.append(int(result[-1]) + int(result[-2]))
            else:
                result.append(int(x))
        sum = 0
        for i in result:
            sum += i
        return sum
