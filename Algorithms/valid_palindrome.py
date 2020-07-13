class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        
        s = s.lower()
        
        subcounter = 0
        placer = len(s)-1
        
        for i in range(len(s)):
            
            if s[i].isalnum():
                while not s[placer].isalnum():
                    placer -= 1


                if s[i]!=s[placer]:
                    return False

                if placer == i:
                    break

                placer-=1

        return True
                