class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        dict_minus = { "IV":2, "IX":2, "XL":20, "XC":20, "CD":200, "CM":200}
        sum = 0
        for word in s:
            sum += dict[word]
        for i in range(len(s) - 1):
            word_combined = s[i] + s[i+1]
            if word_combined in dict_minus:
                sum -= dict_minus[word_combined]
        return sum
