import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy_servers = []
        
        available_servers = list(range(k))
        
        request_counts = [0] * k
        
        for i, (start_time, duration) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= start_time:
                _, server_id = heapq.heappop(busy_servers)
                idx = bisect.bisect_left(available_servers, server_id)
                available_servers.insert(idx, server_id)
            
            if not available_servers:
                continue
            
            target = i % k
            idx = bisect.bisect_left(available_servers, target)
            
            if idx == len(available_servers):
                idx = 0
            
            server_id = available_servers.pop(idx)
            
            request_counts[server_id] += 1
            heapq.heappush(busy_servers, (start_time + duration, server_id))
            
        max_requests = max(request_counts)
        
        return [i for i, count in enumerate(request_counts) if count == max_requests]