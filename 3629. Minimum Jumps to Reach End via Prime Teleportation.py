import collections

class Solution:
    
    MAX_VAL = 10**6 + 1
    _spf = list(range(MAX_VAL))
    _is_prime = [True] * MAX_VAL
    _is_prime[0] = _is_prime[1] = False
    
    for i in range(2, int(MAX_VAL**0.5) + 1):
        if _is_prime[i]:
            for j in range(i*i, MAX_VAL, i):
                _is_prime[j] = False
                if _spf[j] == j:
                    _spf[j] = i

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        
        prime_to_indices = collections.defaultdict(list)
        for i, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = self._spf[temp]
                prime_to_indices[p].append(i)
                while temp % p == 0:
                    temp //= p
        
        queue = collections.deque([(0, 0)])
        visited_indices = {0}
        visited_primes = set()
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == n - 1:
                return steps
            
            for neighbor in [curr - 1, curr + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    visited_indices.add(neighbor)
                    queue.append((neighbor, steps + 1))
            
            val = nums[curr]
            if val > 1 and self._is_prime[val]:
                if val not in visited_primes:
                    for target in prime_to_indices[val]:
                        if target not in visited_indices:
                            visited_indices.add(target)
                            queue.append((target, steps + 1))
                    
                    prime_to_indices[val] = []
                    visited_primes.add(val)
                    
        return -1