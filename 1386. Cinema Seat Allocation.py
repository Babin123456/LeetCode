from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                occupied[r] |= (1 << c)
        
        total_groups = (n - len(occupied)) * 2
        
        for mask in occupied.values():
            left = not (mask & 0b0000111100)
            right = not (mask & 0b1111000000)
            middle = not (mask & 0b0011110000)
            
            if left and right:
                total_groups += 2
            elif left or right or middle:
                total_groups += 1
                
        return total_groups
