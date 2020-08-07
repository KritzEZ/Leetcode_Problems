import re

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word.islower() or word.isupper() or (word[:1].isupper() and word[1:].islower()) : return True
        
        return False