class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False 
        
        char_dict = {}
        already_taken = []
        
        for i in range (len(s)):
            if not char_dict.has_key(s[i]):
                char_dict[s[i]] = t[i]
                if t[i] in already_taken:
                    return False
                already_taken.append(t[i])
            else:
                if char_dict.get(s[i]) != t[i]:
                    return False
        return True