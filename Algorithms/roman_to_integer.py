class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sub_instances = ["IV", "IX", "XL", "XC", "CD", "CM"]
        
        symbol_val = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000 }
        
        sum = 0
        i=0
        while i < len(s):
            if i <= len(s)-2 and (s[i] + s[i+1]) in sub_instances:
                sum += (symbol_val.get(s[i+1]) - symbol_val.get(s[i]))
                i+=1
            else:
                sum += symbol_val.get(s[i])
            i+=1
            
        return sum