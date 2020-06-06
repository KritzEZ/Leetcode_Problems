class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or "" in strs: return ""
        result = strs[0]
        
        for word in strs:
            good_len = min(len(result), len(word))
            temp = result
            for i in range(good_len):
                if temp[i] != word[i]:
                    result = temp[:i]
                    break
                result = temp[:i+1]
        return result
        