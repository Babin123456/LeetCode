from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)

        odd = [ch for ch, count in freq.items() if count % 2]

        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else ""

        cnt = [0] * 26
        for ch, count in freq.items():
            cnt[ord(ch) - ord('a')] = count // 2

        half_len = n // 2
        prefix = []

        def build_suffix():
            return ''.join(
                chr(ord('a') + i) * cnt[i]
                for i in range(26)
            )

        for i in range(half_len):
            cur = ord(target[i]) - ord('a')

            if cnt[cur] > 0:
                prefix.append(target[i])
                cnt[cur] -= 1
                continue

            for j in range(cur + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    left = ''.join(prefix) + chr(ord('a') + j) + build_suffix()
                    return left + mid + left[::-1]

            break
        else:
            left = ''.join(prefix)
            candidate = left + mid + left[::-1]

            if candidate > target:
                return candidate

        while prefix:
            last = prefix.pop()
            cur = ord(last) - ord('a')
            cnt[cur] += 1

            for j in range(cur + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1

                    left = (
                        ''.join(prefix)
                        + chr(ord('a') + j)
                        + build_suffix()
                    )

                    return left + mid + left[::-1]

        return ""