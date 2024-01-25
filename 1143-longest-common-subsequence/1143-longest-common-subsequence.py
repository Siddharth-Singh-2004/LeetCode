class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i == 0 or j == 0):
                    arr[i][j] = 0
                elif text2[i-1] == text1[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        return arr[len(text2)][len(text1)]
                    