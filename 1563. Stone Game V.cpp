#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int stoneGameV(std::vector<int>& stoneValue) {
        int n = stoneValue.size();
        if (n <= 1) return 0;

        std::vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + stoneValue[i];
        }

        auto get_sum = [&](int i, int j) {
            return pref[j + 1] - pref[i];
        };

        // dp[i][j]: max score for subarray stoneValue[i..j]
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        // maxL[i][j] = max_{i <= k <= j} (dp[i][k] + sum(i, k))
        std::vector<std::vector<int>> maxL(n, std::vector<int>(n, 0));
        // maxR[i][j] = max_{i <= k <= j} (dp[k][j] + sum(k, j))
        std::vector<std::vector<int>> maxR(n, std::vector<int>(n, 0));

        for (int i = 0; i < n; ++i) {
            maxL[i][i] = stoneValue[i];
            maxR[i][i] = stoneValue[i];
        }

        for (int len = 2; len <= n; ++len) {
            int mid = 0;
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len - 1;
                mid = std::max(mid, i);

                // Advance mid to find the split point where left_sum <= right_sum
                while (mid < j && get_sum(i, mid) * 2 <= get_sum(i, j)) {
                    ++mid;
                }

                int k = mid - 1;
                // If left sum == right sum
                if (k >= i && get_sum(i, k) * 2 == get_sum(i, j)) {
                    dp[i][j] = std::max(maxL[i][k], maxR[k + 1][j]);
                } else {
                    int best = 0;
                    if (k >= i) {
                        best = std::max(best, maxL[i][k]);
                    }
                    if (k + 1 < j) {
                        best = std::max(best, maxR[k + 2][j]);
                    }
                    dp[i][j] = best;
                }

                int total = get_sum(i, j);
                maxL[i][j] = std::max(maxL[i][j - 1], dp[i][j] + total);
                maxR[i][j] = std::max(maxR[i + 1][j], dp[i][j] + total);
            }
        }

        return dp[0][n - 1];
    }
};