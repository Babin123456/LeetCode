class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self.build(data, 2 * node + 1, start, mid)
        self.build(data, 2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, l, r):
        if r < start or end < l or l > r:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node + 1, start, mid, l, r),
                   self.query(2 * node + 2, mid + 1, end, l, r))

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
        segments = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.append((int(s[i]), i, j - 1, j - i))
            i = j
            
        m = len(segments)
        if m == 0:
            return [0] * len(queries)

        full_gain = [0] * m
        for k in range(m):
            if segments[k][0] == 1:
                left_len = segments[k-1][3] if k > 0 else 0
                right_len = segments[k+1][3] if k < m - 1 else 0
                full_gain[k] = left_len + right_len

        seg_tree = SegmentTree(full_gain)
        
        import bisect
        starts = [seg[1] for seg in segments]
        res = []
        
        for l, r in queries:
            seg_l = bisect.bisect_right(starts, l) - 1
            seg_r = bisect.bisect_right(starts, r) - 1

            valid_start = seg_l + 1 if segments[seg_l][0] == 0 else seg_l + 2
            valid_end = seg_r - 1 if segments[seg_r][0] == 0 else seg_r - 2

            if valid_start > valid_end:
                res.append(total_ones)
                continue

            max_gain = 0

            left_0 = (segments[valid_start - 1][2] - l + 1) if (valid_start - 1 == seg_l) else segments[valid_start - 1][3]
            right_0 = (r - segments[valid_start + 1][1] + 1) if (valid_start + 1 == seg_r) else segments[valid_start + 1][3]
            max_gain = max(max_gain, left_0 + right_0)

            if valid_start != valid_end:
                left_0 = (segments[valid_end - 1][2] - l + 1) if (valid_end - 1 == seg_l) else segments[valid_end - 1][3]
                right_0 = (r - segments[valid_end + 1][1] + 1) if (valid_end + 1 == seg_r) else segments[valid_end + 1][3]
                max_gain = max(max_gain, left_0 + right_0)

            if valid_start + 2 <= valid_end - 2:
                max_gain = max(max_gain, seg_tree.query(0, 0, m - 1, valid_start + 2, valid_end - 2))

            res.append(total_ones + max_gain)

        return res