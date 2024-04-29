class Solution(object):
    def networkDelayTime(self, times, n, k):
        import heapq as hq
        from collections import defaultdict
        graph=defaultdict(list)
        for x in times:
            graph[x[0]]+=[(x[1], x[2])]
        dist=[float('infinity') for x in range(n)]
        heap=[(k,0)]
        dist[k-1]=0
        hq.heapify(heap)
        while(heap):
            node, time=hq.heappop(heap)
            for child, weight in graph[node]:
                new_weight=time+weight
                if (new_weight<dist[child-1]):
                    hq.heappush(heap,(child, new_weight))
                    dist[child-1]=new_weight
        max_time= max(dist)
        if max_time==float('infinity'):
            return -1
        print(dist)
        return max_time
if __name__ == "__main__":
    obj=Solution()
    Op=obj.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
    print(Op)
