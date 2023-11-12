import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = set()
        moves = [[-1] * n for _ in range(n)]
        for x, y, z in times:
            moves[x-1][y-1] = z
        k -= 1
        currentQ = []
        heapq.heappush(currentQ, (0, k))
        
        while len(visited)!= n and len(currentQ) != 0:
            priority, item = heapq.heappop(currentQ)
            visited.add(item)
            for i in range(n):
                print(i)
                if moves[item][i] != -1 and i not in visited:
                    heapq.heappush(currentQ, (priority+moves[item][i], i))
        
        if len(visited) != n:
            return -1
        return priority
                
        
        
        