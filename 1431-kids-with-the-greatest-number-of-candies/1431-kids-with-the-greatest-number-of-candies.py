class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)

        for i in range(len(candies)):
            candies[i] += extraCandies

        arr = []
        for i in candies:
            if i < m:
                arr.append(False)
            else:
                arr.append(True)
            
        return arr