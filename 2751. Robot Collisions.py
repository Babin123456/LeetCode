class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # store (pos, health, dir, index)
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)]
        )
        
        stack = []  # indices of robots moving right
        alive = [True] * n
        
        for pos, health, dirc, idx in robots:
            
            if dirc == 'R':
                stack.append(idx)
            
            else:  # moving left
                while stack and alive[idx]:
                    top = stack[-1]
                    
                    if healths[top] < health:
                        alive[top] = False
                        stack.pop()
                        health -= 1
                    
                    elif healths[top] > health:
                        alive[idx] = False
                        healths[top] -= 1
                        break
                    
                    else:  # equal
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break
                
                healths[idx] = health
        
        # collect survivors in original order
        result = []
        for i in range(n):
            if alive[i]:
                result.append(healths[i])
        
        return result