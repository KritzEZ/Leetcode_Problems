class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "qwertyuiop"
        second = "asdfghjkl" 
        third = "zxcvbnm"

        ans = []

        for word in words:
            word1 = word.lower()
            mySet = set()
            for char in word1:
                if char in first:
                    mySet.add("first")
                if char in second:
                    mySet.add("second")
                if char in third:
                    mySet.add("thrid")
            if len(mySet) == 1:
                ans.append(word)

        return ans
