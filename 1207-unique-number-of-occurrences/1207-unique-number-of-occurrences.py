class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num = {}
        for i in arr:
            if i in num:
                num[i] += 1
            else:
                num[i] = 1
              
        flag = True
        for i in num:
            for j in num:
                if i != j:
                    if num[i] == num[j]:
                        flag = False
                        break
        return flag
        