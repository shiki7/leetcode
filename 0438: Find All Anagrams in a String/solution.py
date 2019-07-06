class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        LENGTH = len(p)
        ans = []
        s_counter = collections.Counter(s[:len(p)-1])
        p_counter = collections.Counter(p)
        for i in range(len(p)-1,len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter: 
                ans.append(i-len(p)+1)
            s_counter[s[i-len(p)+1]] -= 1
            if s_counter[s[i-len(p)+1]] == 0:
                del s_counter[s[i-len(p)+1]]
        return ans
                
