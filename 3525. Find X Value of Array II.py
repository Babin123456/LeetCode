from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def _merge(self, node: int, left_node: int, right_node: int):
        l_prod = self.tree_prod[left_node]
        r_prod = self.tree_prod[right_node]
        
        self.tree_prod[node] = (l_prod * r_prod) % self.k
        
        cnt = list(self.tree_cnt[left_node])
        
        r_cnt = self.tree_cnt[right_node]
        for rem in range(self.k):
            if r_cnt[rem] > 0:
                cnt[(l_prod * rem) % self.k] += r_cnt[rem]
                
        self.tree_cnt[node] = cnt

    def build(self, nums: List[int], node: int, start: int, end: int):
        if start == end:
            val_rem = nums[start] % self.k
            self.tree_prod[node] = val_rem
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][val_rem] = 1
            return

        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        self._merge(node, 2 * node + 1, 2 * node + 2)

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            val_rem = val % self.k
            self.tree_prod[node] = val_rem
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][val_rem] = 1
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
            
        self._merge(node, 2 * node + 1, 2 * node + 2)

    def query(self, node: int, start: int, end: int, ql: int, qr: int):
        if ql <= start and end <= qr:
            return self.tree_prod[node], self.tree_cnt[node]

        mid = (start + end) // 2
        if qr <= mid:
            return self.query(2 * node + 1, start, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 2, mid + 1, end, ql, qr)

        l_prod, l_cnt = self.query(2 * node + 1, start, mid, ql, qr)
        r_prod, r_cnt = self.query(2 * node + 2, mid + 1, end, ql, qr)

        res_prod = (l_prod * r_prod) % self.k
        res_cnt = list(l_cnt)
        
        for rem in range(self.k):
            if r_cnt[rem] > 0:
                res_cnt[(l_prod * rem) % self.k] += r_cnt[rem]

        return res_prod, res_cnt


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            st.update(0, 0, n - 1, idx, val)
            _, cnt = st.query(0, 0, n - 1, start, n - 1)
            ans.append(cnt[x])

        return ans
