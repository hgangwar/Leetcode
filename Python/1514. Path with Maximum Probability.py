"""
import heapq
from collections import defaultdict
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        def dijkstra(graph, start):
            distances = [0 for i in range(n)]
            distances[start] = -1
            queue = [(-1, start)]
            heapq.heapify(queue)
            while queue:
                current_distance, current_vertex = heapq.heappop(queue)
                for neighbor, weight in graph[current_vertex]:
                    distance = current_distance * weight
                    if abs(distance) > abs(distances[neighbor]):
                        distances[neighbor] = -abs(distance)
                        heapq.heappush(queue, (-abs(distance), neighbor))
            return distances
        graph=defaultdict(list)
        for i,x in enumerate(edges):
            graph[x[0]]+=[[x[1], succProb[i]]]
            graph[x[1]]+=[[x[0], succProb[i]]]
        shortestpath=dijkstra(graph,start)
        print(shortestpath)
        ans=shortestpath[end]
        return  abs(ans)
"""
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        import heapq
        from collections import defaultdict
        graph=defaultdict(list)
        for i,x in enumerate(edges):
            graph[x[0]]+=[(x[1], -succProb[i])]
            graph[x[1]]+=[(x[0], -succProb[i])]        
        heap=[(-1, start)]
        dist =[0 for x in range(n)]
        dist[start]=-1
        heapq.heapify(heap)
        while (heap):
            weight, node=heapq.heappop(heap)
            for child, p in graph[node]:
                new_weight=-(p*weight)
                if(new_weight < dist[child]):
                    dist[child]=new_weight
                    heapq.heappush(heap, (new_weight, child))
        print(dist)
        return -(dist[end])
if __name__ == "__main__":
    obj=Solution()
    Op=obj.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
    print(Op)