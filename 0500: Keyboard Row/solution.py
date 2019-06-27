class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list1 = ['q','w','e','r','t','y','u','i','o','p']
        list2 = ['a','s','d','f','g','h','j','k','l']
        list3 = ['z','x','c','v','b','n','m']
        ans = []
        for word in words:
            word.lower()
            char_count1 = char_count2 = char_count3 = 0
            for char in word:
                if char in list1:
                    char_count1 +=1
                if char in list2:
                    char_count2 +=1
                if char in list3:
                    char_count3 +=1
            if (char_count1 > 0 and char_count2 == 0 and char_count3 == 0) or (char_count1 == 0 and char_count2 > 0 and char_count3 == 0) or (char_count1 == 0 and char_count2 == 0 and char_count3 > 0):
                ans += [word]
        return ans
