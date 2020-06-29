class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """        
        
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] += 1
            return digits
        
        else:
            carry = True
            for i in range(len(digits)-1, -1, -1):
                if digits[i] != 9:
                    digits[i] += 1
                    return digits   
                digits[i] = 0
                if i == 0: digits.insert(0, 1)
        return digits