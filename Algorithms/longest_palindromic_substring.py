class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1 or s == s[::-1]: return s
        
        longest = s[0]
        for i in range(len(s)):
            curr_long = s[i]
            for j in range(i+1, len(s)):
                curr_long += s[j]
                if curr_long == curr_long[::-1] and len(curr_long) > len(longest):
                    longest = curr_long
                    if len(curr_long) == len(s)-i:
                        break
            
        return longest