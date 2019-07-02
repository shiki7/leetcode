class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        for i in range(1,len(word_list)+1):
            if word_list[-i] != "":
                return len(word_list[-i])
        return 0
