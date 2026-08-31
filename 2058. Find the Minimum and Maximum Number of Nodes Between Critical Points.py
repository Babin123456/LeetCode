class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        nxt = curr.next

        index = 1
        first_crit_idx = -1
        prev_crit_idx = -1
        min_dist = float('inf')

        while nxt:
            is_critical = (curr.val > prev.val and curr.val > nxt.val) or \
                          (curr.val < prev.val and curr.val < nxt.val)

            if is_critical:
                if first_crit_idx == -1:
                    first_crit_idx = index
                else:
                    min_dist = min(min_dist, index - prev_crit_idx)
                
                prev_crit_idx = index

            prev = curr
            curr = nxt
            nxt = nxt.next
            index += 1

        if first_crit_idx == prev_crit_idx:
            return [-1, -1]

        max_dist = prev_crit_idx - first_crit_idx
        return [min_dist, max_dist]