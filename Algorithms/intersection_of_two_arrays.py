class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        intersect = []
        
        minlen = min(len(nums1), len(nums2))
        
        for i in range(minlen):
            if nums1[i] in nums2 and nums1[i] not in intersect and minlen == len(nums1):
                intersect.append(nums1[i])
                nums1[nums1.index(nums2[i])] = None
                
            elif nums2[i] in nums1 and nums2[i] not in intersect and minlen == len(nums2):
                intersect.append(nums2[i])                
                nums1[nums1.index(nums2[i])] = None
                
        return intersect