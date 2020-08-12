class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        listS = list(s)
        
        start = 0
        end = len(s)-1
        
        while start < end:
            if listS[start].lower() in vowels and listS[end].lower()  in vowels:
                listS[start], listS[end] = listS[end], listS[start]
                start += 1
                end -= 1
                
            elif listS[start].lower()  in vowels:
                end -= 1
                
            elif listS[end].lower()  in vowels:
                start += 1
                
            else:
                start += 1
                end -+ 1
                
        return "".join(listS)