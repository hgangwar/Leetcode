class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        from collections import defaultdict
        import heapq as hq
        graph=defaultdict(list)
        for x in edges:
            graph[x[0]]+=[(x[1],x[2])]
            graph[x[1]]+=[(x[0],x[2])]
        cities=[set() for x in range(n)]
        
        for src in range(n):
            heap=[(-distanceThreshold, src)]
            hq.heapify(heap)
            d_left=[0 for x in range(n)]
            while(heap):
                dist, node=hq.heappop(heap)
                for child, weight in graph[node]:
                    new_weight=abs(dist)-weight
                    if (new_weight>=d_left[child] and child!=src):
                        d_left[child]=new_weight
                        hq.heappush(heap,(-new_weight, child))
                        cities[src].add(child)
        ans=0
        min_city=n
        #print(graph)
        #print(cities)
        for i,x in enumerate(cities):
            if(min_city>=len(x)):
                min_city=len(x)
                ans=i
        return ans
if __name__ == "__main__":
    obj=Solution()
    Op=obj.findTheCity(n = 6, edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], distanceThreshold = 20)
    print(Op)

        