class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)
        binary_fixed = binary.lstrip("0b")
        before_one_existed = False
        max_distance = 0
        distance = 0
        for number in str(binary_fixed):
            if number == "1" and not before_one_existed:
                before_one_existed = True
            elif number == "1" and before_one_existed:
                distance += 1
                if max_distance < distance:
                    max_distance = distance
                distance = 0
            elif number == "0" and before_one_existed:
                    distance += 1       
        return max_distance
