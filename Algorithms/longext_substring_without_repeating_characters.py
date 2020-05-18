def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        library = []
        for i in range(len(s)):
            if s[i] in library:
                library = library[library.index(s[i])+1:]
            
            library.append(s[i])
            if len(library) > longest: longest = len(library)
                
        return longest