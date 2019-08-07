class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stock5, stock10 = 0, 0
        for bill in bills:
            if bill == 5:
                stock5 += 1
                continue
            elif bill == 10:
                if stock5 == 0:
                    return False
                stock5 -= 1
                stock10 += 1
            elif bill == 20:
                if stock5 >= 1 and stock10 >= 1:
                    stock10 -= 1
                    stock5 -= 1
                elif stock5 >= 3 and stock10 == 0:
                    stock5 -= 3
                else:
                    return False
        return True
