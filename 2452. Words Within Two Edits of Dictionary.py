class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []

        for query in queries:
            for word in dictionary:
                edits = 0
                for i in range(n):
                    if query[i] != word[i]:
                        edits += 1

                if edits <= 2:
                    res.append(query)
                    break

        return res
