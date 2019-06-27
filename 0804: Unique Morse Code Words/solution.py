class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list = []
        for word in words:
            morse_str = ""
            for char in word:
                morse_str += MORSE[ord(char) - 97]
            if morse_str not in list:
                list.append(morse_str)
        return len(list)
