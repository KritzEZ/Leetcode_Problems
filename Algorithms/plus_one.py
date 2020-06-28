class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[len(digits)-1-i] < 9:
                digits[len(digits)-1-i] += 1
                return digits
            else:
                digits[len(digits)-1-i] = 0

            digits.insert(0, 1)
            return digits
            
        

            
