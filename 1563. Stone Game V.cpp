class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, val in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + val

        dp = [[0] * n for _ in range(n)]
        
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            k = 0
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]

                if i == 0 or k < i:
                    k = i
                while k < j and (prefix[k + 1] - prefix[i]) * 2 <= total:
                    k += 1
                
                mid = k - 1
                res = 0
                
                if mid >= i:
                    res = max(res, max_left[i][mid])
                
                if mid >= i and (prefix[mid + 1] - prefix[i]) * 2 == total:
                    res = max(res, max_right[mid + 1][j])
                
                right_start = mid + 1
                if (prefix[mid + 1] - prefix[i]) * 2 == total:
                    right_start += 1
                if right_start <= j:
                    res = max(res, max_right[right_start][j])

                dp[i][j] = res
                max_left[i][j] = max(max_left[i][j - 1], res + total)
                max_right[i][j] = max(max_right[i + 1][j], res + total)

        return dp[0][n - 1]
