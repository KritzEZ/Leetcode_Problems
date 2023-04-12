class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if s == goal:
            return True

        sSplit = list(s)
        goalSplit = list(goal)

        for i in range (len(s)):
            temp = sSplit[0]
            sSplit.pop(0)
            sSplit.append(temp)

            if sSplit == goalSplit:
                return True
        
        return False