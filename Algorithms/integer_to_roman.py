class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        val_dict = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        
        answer = ""
        
        while num > 0:
            for i in range(len(values)):
                if num-values[i] >= 0:
                    answer += val_dict.get(values[i])
                    num -= values[i]
                    values = values[i:len(values)]
                    break
        return answer