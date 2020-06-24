class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        letter_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                       '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        answers = []
        
        if len(digits) == 0: return answers
        
        def getcombs(remaining, curr = ""):
            if remaining == "":
                answers.append(curr)
            else:
                for char in letter_dict[remaining[0]]:
                    getcombs(remaining[1:], curr + char)
        
        getcombs(digits)
        return answers