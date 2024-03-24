class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = s.split()
        print(n)
        n = n[::-1]
        return " ".join(n)