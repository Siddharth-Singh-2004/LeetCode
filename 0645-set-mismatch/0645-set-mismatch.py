class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        error = []
        for i in range(1, len(nums)+1):
            if nums.count(i) > 1:
                error.append(i)
        
        for j in range(1, len(nums)+1):
            if j not in nums:
                error.append(j)
        return error
                
                