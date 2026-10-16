class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_down(node, l, r):
            if lazy[node] != 0:
                val = lazy[node]
                mid = (l + r) // 2
                
                # Left child
                left_node = 2 * node
                length_left = mid - l + 1
                tree_sq[left_node] = (tree_sq[left_node] + 2 * val * tree_sum[left_node] + val * val * length_left) % MOD
                tree_sum[left_node] = (tree_sum[left_node] + val * length_left) % MOD
                lazy[left_node] = (lazy[left_node] + val) % MOD
                
                # Right child
                right_node = 2 * node + 1
                length_right = r - mid
                tree_sq[right_node] = (tree_sq[right_node] + 2 * val * tree_sum[right_node] + val * val * length_right) % MOD
                tree_sum[right_node] = (tree_sum[right_node] + val * length_right) % MOD
                lazy[right_node] = (lazy[right_node] + val) % MOD
                
                lazy[node] = 0

        def push_up(node):
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
                tree_sum[node] = (tree_sum[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            push_up(node)

        last_occurrence = {}
        total_sum_squares = 0
        current_total = 0
        
        for i, x in enumerate(nums):
            prev_idx = last_occurrence.get(x, -1)
            update(1, 0, n - 1, prev_idx + 1, i, 1)
            last_occurrence[x] = i
            
            total_sum_squares = (total_sum_squares + tree_sq[1]) % MOD
            
        return total_sum_squares