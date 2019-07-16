class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = []
        result = ''
        for word in words:
            reversed_words += reversed(word)
            reversed_words += " "
        for word in reversed_words:
            result += word
        return result.rstrip()
