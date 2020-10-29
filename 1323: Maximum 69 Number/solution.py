class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        ans = ''
        flg = False
        for i in range(len(str_num)):
            if flg:
                ans += str_num[i:]
                break
            if str_num[i] == '6':
                ans += '9'
                flg = True
            else:
                ans += str_num[i]
        return int(ans)
