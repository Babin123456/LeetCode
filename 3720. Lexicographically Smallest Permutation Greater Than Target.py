from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        prefix = []

        i = 0
        n = len(s)

        while i < n and cnt[target[i]] > 0:
            cnt[target[i]] -= 1
            prefix.append(target[i])
            i += 1

        for pos in range(i, -1, -1):

            if pos < n:
                for c in range(ord(target[pos]) - ord('a') + 1, 26):
                    ch = chr(ord('a') + c)

                    if cnt[ch] > 0:
                        cnt[ch] -= 1

                        suffix = []

                        for j in range(26):
                            char = chr(ord('a') + j)
                            suffix.append(char * cnt[char])

                        return ''.join(prefix[:pos]) + ch + ''.join(suffix)

            if pos > 0:
                cnt[prefix[pos - 1]] += 1

        return ""
