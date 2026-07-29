from collections import Counter

class Solution:

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = Counter(s)

        half_counts = [freq[chr(ord("a") + i)] // 2 for i in range(26)]
        half_len = n // 2

        mid_char = ""
        if n % 2 == 1:
            for i in range(26):
                if freq[chr(ord("a") + i)] % 2 == 1:
                    mid_char = chr(ord("a") + i)
                    break

        def get_combinations(counts, cap):
            total = sum(counts)
            if total == 0:
                return 1

            max_c = max(counts)
            if max_c == total:
                return 1

            ans = 1
            cur_n = total
            max_found = False

            for c in counts:
                if c == 0:
                    continue
                if c == max_c and not max_found:
                    max_found = True
                    continue
                for j in range(1, c + 1):
                    ans = (ans * cur_n) // j
                    cur_n -= 1
                    if ans >= cap:
                        return cap
            return ans

        if get_combinations(half_counts, k + 1) < k:
            return ""

        first_half = []
        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue

                half_counts[i] -= 1
                cnt = get_combinations(half_counts, k + 1)

                if cnt >= k:
                    first_half.append(chr(ord("a") + i))
                    break
                else:
                    k -= cnt
                    half_counts[i] += 1  

        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]