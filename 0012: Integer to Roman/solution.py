class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        ans = ""
        for k in reversed(list(dict.keys())):
            if num/k >= 1:
                ans += dict[k] * int(num/k)
                num = num % k
        return ans
