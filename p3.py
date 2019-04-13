class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        s_length = len(s)
        uniq = ""
        check_start_index = 0
        
        for char in s:
            if char not in uniq:
                uniq += char
                max_length = max(max_length, len(uniq))
            else:
                check_start_index = uniq.index(char) +1
                uniq = uniq[check_start_index:] + char
        return max_length
