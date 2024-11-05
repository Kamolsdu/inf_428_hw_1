class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        result = list(s1 & s2)
        
        return result
