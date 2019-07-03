class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
        vowel_list = []
        ans = ''
        for char in s:
            if char in VOWELS:
                vowel_list += [char]
        for char in s:
            if char in VOWELS:
                ans += vowel_list.pop(-1)
            else:
                ans += char
        return ans
