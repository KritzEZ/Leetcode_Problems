class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """ 
    
        intersect = []
        
        minlen = min(len(nums1), len(nums2))
        
        len1, len2 = len(nums1), len(nums2)
        
        for i in range(minlen):
            if i<len(nums1) and nums1[i] in nums2 and minlen == len1:
                nums2.remove(nums1[i])
                intersect.append(nums1[i])
                
            elif i<len(nums2) and nums2[i] in nums1 and minlen == len2:
                nums1.remove(nums2[i])
                intersect.append(nums2[i])
                
            if len(nums1) == 0 or len(nums2) == 0:
                break
                
        return intersect