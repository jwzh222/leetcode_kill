#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) == 0):
            return False
        nums1 = list(set(nums))
        return len(nums1) != len(nums)
