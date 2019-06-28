class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        word_list = text.split(" ")
        first_check = False
        second_check = False
        third_list = []
        for word in word_list:
            if first_check and second_check:
                third_list += [word]
                first_check = second_check = False
            if word == first:
                first_check = True
            elif first_check and word == second:
                second_check = True
            else:
                first_check = second_check = False
        return third_list          
