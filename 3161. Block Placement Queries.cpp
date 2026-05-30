#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int bit[50005];
    int M = 50001;

    void update(int idx, int val) {
        for (; idx <= M; idx += idx & -idx) bit[idx] = max(bit[idx], val);
    }

    int query(int idx) {
        int mx = 0;
        for (; idx > 0; idx -= idx & -idx) mx = max(mx, bit[idx]);
        return mx;
    }

    vector<bool> getResults(vector<vector<int>>& queries) {
        set<int> obs = {0, M};
        // Step 1: Insert all obstacles to find the final state
        for (auto& q : queries) {
            if (q[0] == 1) obs.insert(q[1]);
        }

        // Step 2: Initialize the Fenwick tree with the final gaps
        fill(bit, bit + M + 1, 0);
        auto it = obs.begin();
        int prev = *it;
        for (++it; it != obs.end(); ++it) {
            update(*it, *it - prev);
            prev = *it;
        }

        vector<bool> ans;
        // Step 3: Process queries backwards
        for (int i = queries.size() - 1; i >= 0; --i) {
            int type = queries[i][0];
            int x = queries[i][1];

            if (type == 1) {
                // Remove obstacle x and merge the gaps
                auto it = obs.find(x);
                int r = *next(it);
                int l = *std::prev(it);
                obs.erase(it);
                update(r, r - l); // The gap at r expands!
            } else {
                int sz = queries[i][2];
                int max_gap = query(x);
                int last_gap = x - *std::prev(obs.lower_bound(x));
                ans.push_back(max(max_gap, last_gap) >= sz);
            }
        }

        // Step 4: Reverse the results back to correct order
        reverse(ans.begin(), ans.end());
        return ans;
    }
};