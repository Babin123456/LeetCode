class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        maskA = 0
        maskB = 0
        res = []
        
        for a, b in zip(A, B):
            maskA |= (1 << a)
            maskB |= (1 << b)
            res.append(bin(maskA & maskB).count("1"))
            
        return res