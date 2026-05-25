from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        queue = deque([0])
        
        for i in range(1, len(s)):
            if s[i] == '0':
                while queue and queue[0] < i - maxJump:
                    queue.popleft()
                
                if queue and queue[0] <= i - minJump:
                    if i == len(s) - 1:
                        return True
                    queue.append(i)
                    
        return False