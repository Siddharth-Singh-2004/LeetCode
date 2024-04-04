class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append("(")
                m = max(m, len(stack))
            elif i == ")":
                stack.pop()
            
        return m
        