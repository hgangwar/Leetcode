import heapq
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n,k):
        def dijkstra(graph, start):
            distances = [float('infinity') for i in range(n)]
            distances[start-1] = 0
            queue = [(0, start)]
            while queue:
                current_distance, current_vertex = heapq.heappop(queue)
                if current_distance > distances[current_vertex-1]:
                    continue
                for neighbor, weight in graph[current_vertex]:
                    distance = current_distance + weight
                    if distance < distances[neighbor-1]:
                        distances[neighbor-1] = distance
                        heapq.heappush(queue, (distance, neighbor))
            return distances
        graph=defaultdict(list)
        for x in times:
            graph[x[0]]+=[x[1:]]
        shortestpath=dijkstra(graph,k)
        ans=max(shortestpath)
        if n!=len(shortestpath) or ans==float('infinity'): return -1
        return  ans
if __name__ == "__main__":
    obj=Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]] 
    n = 4 
    k = 2
    Op=obj.networkDelayTime(times,n,k)
    print(Op)
