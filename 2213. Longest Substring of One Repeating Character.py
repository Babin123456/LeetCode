class SegmentTree:

  def __init__(self, s: str):
    self.n = len(s)
    self.tree = [None] * (4 * self.n)
    self.build(s, 0, 0, self.n - 1)

  def merge(self, left, right, left_size, right_size):
    l_pref, l_suff, l_max, l_lc, l_rc = left
    r_pref, r_suff, r_max, r_lc, r_rc = right

    res_lc = l_lc
    res_rc = r_rc

    res_pref = l_pref
    if l_pref == left_size and l_rc == r_lc:
      res_pref = left_size + r_pref

    res_suff = r_suff
    if r_suff == right_size and l_rc == r_lc:
      res_suff = right_size + l_suff

    res_max = max(l_max, r_max)
    if l_rc == r_lc:
      res_max = max(res_max, l_suff + r_pref)

    return (res_pref, res_suff, res_max, res_lc, res_rc)

  def build(self, s: str, node: int, start: int, end: int):
    if start == end:
      ch = s[start]
      self.tree[node] = (1, 1, 1, ch, ch)
      return

    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2

    self.build(s, left_node, start, mid)
    self.build(s, right_node, mid + 1, end)

    left_size = mid - start + 1
    right_size = end - mid
    self.tree[node] = self.merge(
        self.tree[left_node], self.tree[right_node], left_size, right_size
    )

  def update(self, node: int, start: int, end: int, idx: int, ch: str):
    if start == end:
      self.tree[node] = (1, 1, 1, ch, ch)
      return

    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2

    if idx <= mid:
      self.update(left_node, start, mid, idx, ch)
    else:
      self.update(right_node, mid + 1, end, idx, ch)

    left_size = mid - start + 1
    right_size = end - mid
    self.tree[node] = self.merge(
        self.tree[left_node], self.tree[right_node], left_size, right_size
    )

class Solution:

  def longestRepeating(
      self, s: str, queryCharacters: str, queryIndices: list[int]
  ) -> list[int]:
    st = SegmentTree(s)
    ans = []

    for char, idx in zip(queryCharacters, queryIndices):
      st.update(0, 0, len(s) - 1, idx, char)
      ans.append(st.tree[0][2])  # max_len at root node

    return ans