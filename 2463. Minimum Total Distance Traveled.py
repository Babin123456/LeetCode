class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i == len(robot):
                return 0

            if j == len(factory):
                return float('inf')

            res = dp(i, j + 1)

            pos, limit = factory[j]
            cost = 0

            for k in range(1, limit + 1):
                if i + k > len(robot):
                    break

                cost += abs(robot[i + k - 1] - pos)

                res = min(res, cost + dp(i + k, j + 1))

            return res

        return dp(0, 0)