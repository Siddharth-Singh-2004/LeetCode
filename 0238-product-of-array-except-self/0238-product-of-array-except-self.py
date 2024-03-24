class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 1
        for i in nums:
            m *= i
            
        arr = []
        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(m//nums[i])
            else:
                temp = 1
                for j in range(len(nums)):
                    if j != i:
                        temp *= nums[j]
                arr.append(temp)
        return arr
        
        