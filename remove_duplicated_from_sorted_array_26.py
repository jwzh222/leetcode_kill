class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if (length <= 1):
            return length
        tmp = nums[0]
        i = 1
        while (i < length):
            if (nums[i] == tmp):
                del nums[i]
                length -= 1
            else:
                tmp = nums[i]
                i+=1
        return len(nums)