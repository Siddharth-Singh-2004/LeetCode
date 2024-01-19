class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        columns = len(matrix[0])
        prev = matrix[0][:]
        for r in range(1, len(matrix)):
            current = [0] * columns
            for c in range(columns):
                element = matrix[r][c]
                top = element + prev[c] 
                topL = element + prev[c-1] if c > 0 else float('inf')
                topR = element + prev[c+1] if c < columns-1 else float('inf')
                current[c] = min(top, topL, topR)
            prev = current

        return min(prev)        
        
            
            
        