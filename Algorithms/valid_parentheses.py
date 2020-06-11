class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        m = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                m.append(s[i])
            else:
                if len(m) >= 1:
                    if s[i] == ')' and m[len(m)-1] == '(':
                        m = m[:len(m)-1]
                    elif s[i] == '}' and m[len(m)-1] == '{':
                        m = m[:len(m)-1]
                    elif s[i] == ']' and m[len(m)-1] == '[':
                        m = m[:len(m)-1]
                        
                    else: return False
                    
                else: return False
                
        if len(m) == 0:
            return True
        else: return False