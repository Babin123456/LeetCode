class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = 1500
        mult_count = [0] * (max_f + 1)
        exact_count = [0] * (max_f + 1)

        for factor, _ in items:
            exact_count[factor] += 1

        for f in range(1, max_f + 1):
            total = 0
            for m in range(f, max_f + 1, f):
                total += exact_count[m]
            mult_count[f] = total

        dp = [0] * (budget + 1)

        for factor, price in items:
            if price > budget:
                continue
            freebies = mult_count[factor] - 1
            first_gain = 1 + freebies
            next_dp = dp[:]

            for b in range(price, budget + 1):
                if dp[b - price] + first_gain > next_dp[b]:
                    next_dp[b] = dp[b - price] + first_gain

            for b in range(price, budget + 1):
                if next_dp[b - price] + 1 > next_dp[b]:
                    next_dp[b] = next_dp[b - price] + 1

            dp = next_dp

        return max(dp)