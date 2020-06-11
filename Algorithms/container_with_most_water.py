class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxvol = 0
        start, end = 0, len(height)-1
        
        while True:
            
            vol = min(height[start], height[end]) * abs(start-end)
            if height[start]<height[end]: start += 1
            else: end -= 1
                
            if vol > maxvol: maxvol = vol
                
            if start == end: break
        return maxvol