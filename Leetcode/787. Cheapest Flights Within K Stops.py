from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        def dijkstra():
            cost = [float('infinity') for i in range(n)]
            cost[src] = 0
            queue = [(0, 0,src)]
            while queue:
                current_cost, steps, curr_state = queue.pop(0)
                for neighbor, weight in graph[curr_state]:
                    newCost = current_cost + weight
                    if newCost < cost[neighbor] and steps<=k:
                        cost[neighbor] = newCost
                        queue.append([cost[neighbor], steps+1, neighbor])
            return cost[dst]
        graph=defaultdict(list)
        for x in flights:
            graph[x[0]]+=[x[1:]]
        Price=dijkstra()
        if Price==float('infinity'): return -1
        return Price
if __name__ == "__main__":
    obj=Solution()
    n = 11
    flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    src=0
    dst=2
    k = 4
    Op=obj.findCheapestPrice(n,flights,src,dst,k)
    print(Op)