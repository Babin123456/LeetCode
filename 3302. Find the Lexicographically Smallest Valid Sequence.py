class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        last_pos = [-1] * m
        
        i = n - 1
        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1
            if i >= 0:
                last_pos[j] = i
                i -= 1

        result = []
        used_change = False
        i = 0
        
        for j in range(m):
            while i < n:
                if word1[i] == word2[j]:
                    result.append(i)
                    i += 1
                    break
                
                if not used_change:
                    can_finish = (j == m - 1) or (last_pos[j + 1] > i)
                    if can_finish:
                        used_change = True
                        result.append(i)
                        i += 1
                        break
                
                i += 1

        return result if len(result) == m else []