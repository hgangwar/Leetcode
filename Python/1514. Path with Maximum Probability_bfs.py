class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        def build_graph(n, edges, probability):
            graph = {}
            for i in range(n):
                graph[i] = []
            for i in range(len(edges)):
                frm, to = edges[i]
                graph[frm].append((probability[i], to))
                graph[to].append((probability[i], frm))
            return graph
        def bfs(graph):
            import heapq as hq
            dist = {start:-1}
            heap = [(-1, start)]
            hq.heapify(heap)
            while len(heap) > 0:
                prob, node = hq.heappop(heap)
                for child in graph[node]:
                    p,c = child
                    if c in dist:
                        if abs(p*prob) > abs(dist[c]):
                            hq.heappush(heap, (-abs(p*prob), c))
                            dist[c] = -abs(p*prob)
                    else:
                        hq.heappush(heap, (-abs(p * prob), c))
                        dist[c] = -abs(p * prob)
            return 0 if end not in dist else -dist[end]
        return bfs(build_graph(n, edges, succProb))
if __name__ == "__main__":
    obj=Solution()
    Op=obj.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
    print(Op)