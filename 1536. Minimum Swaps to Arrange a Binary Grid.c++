#pragma GCC optimize("O2")

#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int minSwaps(vector<vector<int>> &grid)
    {
        int n = grid.size();

        vector<int> endZeros(n);

        for (int i = 0; i < n; i++)
        {
            int count = 0;
            for (int j = n - 1; j >= 0; j--)
            {
                if (grid[i][j] == 0)
                    count++;
                else
                    break;
            }
            endZeros[i] = count;
        }

        int steps = 0;

        for (int i = 0; i < n; i++)
        {

            int need = n - i - 1;
            int j = i;

            while (j < n && endZeros[j] < need)
            {
                j++;
            }

            if (j == n)
            {
                return -1;
            }

            while (j > i)
            {
                swap(endZeros[j], endZeros[j - 1]);
                steps++;
                j--;
            }
        }

        return steps;
    }
};