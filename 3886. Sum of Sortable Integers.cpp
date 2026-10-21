#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int sortableIntegers(std::vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;

        for (int k = 1; k <= n; ++k) {
            if (n % k != 0) continue;

            bool isSortable = true;
            int prevMax = -1;

            for (int i = 0; i < n; i += k) {
                int blockMin = nums[i];
                int blockMax = nums[i];
                int drops = 0;

                for (int j = i; j < i + k; ++j) {
                    blockMin = std::min(blockMin, nums[j]);
                    blockMax = std::max(blockMax, nums[j]);

                    if (j < i + k - 1 && nums[j] > nums[j + 1]) {
                        drops++;
                    }
                }

                if (prevMax > blockMin) {
                    isSortable = false;
                    break;
                }

                if (drops > 1) {
                    isSortable = false;
                    break;
                }
                if (drops == 1 && nums[i + k - 1] > nums[i]) {
                    isSortable = false;
                    break;
                }

                prevMax = blockMax;
            }

            if (isSortable) {
                totalSum += k;
            }
        }

        return totalSum;
    }
};