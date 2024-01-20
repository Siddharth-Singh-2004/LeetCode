class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        stack = []
        sum_result = 0
        dp = [0] * len(arr)

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                left = stack[-1] if stack else -1
                dp[cur] = (i - cur) * (cur - left)

            stack.append(i)

        # Process remaining elements in the stack
        while stack:
            cur = stack.pop()
            left = stack[-1] if stack else -1
            dp[cur] = (len(arr) - cur) * (cur - left)

        # Calculate the sum using the precomputed dp array
        for i in range(len(arr)):
            sum_result += arr[i] * dp[i]

        return sum_result % MOD
        
        