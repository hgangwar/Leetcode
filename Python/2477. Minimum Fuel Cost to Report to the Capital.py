from collections import defaultdict
class Solution(object):
    def minimumFuelCost(self, roads, seats):
        n=len(roads)+1
        Map=defaultdict(list)
        for x in roads:
            Map[x[0]]+=[x[1]]
            Map[x[1]]+=[x[0]]
        if not roads: return 0
        visited=[True]*(n+1)
        self.totalfuel=0
        def dfs(src):
            total_reps=0
            visited[src]=False
            for x in Map[src]:
                if visited[x]:
                    reps=dfs(x)
                else: continue
                if reps%seats==0:  
                    self.totalfuel+=reps/seats
                else:
                    self.totalfuel+=(reps//seats)+1
                total_reps+=reps
            return total_reps+1
        dfs(0)
        return int(self.totalfuel)
if __name__ == "__main__":
    obj=Solution()
    Op=obj.minimumFuelCost([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2)
    print(Op)