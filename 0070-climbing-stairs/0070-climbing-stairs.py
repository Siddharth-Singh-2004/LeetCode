class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 1
        x = 0
        for i in range(2, n+1):
            x = a + b
            a = b
            b = x
        return x


        
        