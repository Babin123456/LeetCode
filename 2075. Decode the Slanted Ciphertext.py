class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        res = ''

        for j in range(cols):
            for i in range(rows):
                if i + j >= cols: break
                res += encodedText[i * cols + (j + i)]

        return res.rstrip()