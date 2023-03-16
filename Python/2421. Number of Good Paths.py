from collections import Counter, defaultdict
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.e = 0

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1

        if px > py:
            self.p[px] = py
        else:
            self.p[py] = px
        self.e += 1
        return 0
class Solution:
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)
        uf = DSU(n)
        e = defaultdict(list)
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        value_indices = defaultdict(list)
        for i, v in enumerate(vals):
            value_indices[v].append(i)
        ans = n
        for v in sorted(value_indices.keys()):
            for i in value_indices[v]:
                for j in e[i]:
                    if vals[j] <= v:
                        uf.union(i, j)
            c = Counter()
            for i in value_indices[v]:
                p = uf.find(i)
                c[p] += 1

            for _, count in c.items():
                if count > 1:
                    ans += count * (count - 1) // 2
        return ans
if __name__ == "__main__":
    obj=Solution()
    vals = [2,5,5,1,5,2,3,5,1,5]
    edges = [[0,1],[2,1],[3,2],[3,4],[3,5],[5,6],[1,7],[8,4],[9,7]]
    Op=obj.numberOfGoodPaths(vals,edges)
    print(Op)

""" naive : dfs from src to end
from collections import defaultdict
class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        graph=defaultdict(list)
        Vg=defaultdict(list)
        n=len(vals)
        for x in edges:
            graph[x[0]]+=[x[1]]
            graph[x[1]]+=[x[0]]
        for i,x in enumerate(vals):
            Vg[x]+=[i]
        count=0
        def traverse(src,end,path):
            res=0
            localpath=[src]
            if(src==end):
                return 1
            elif(vals[src]>vals[end]):
                return 0
            for x in graph[src]:
                if not (x in path):
                    res=traverse(x,end,localpath+path)
                if(res==1): return res
            return res
        for x in Vg.keys():
            if len(Vg[x])==1: continue
            temp=dict()
            for i in Vg[x]:
                for j in Vg[x]:
                    key= tuple([min(i,j),max(i,j)])
                    if(key in temp or i==j): continue
                    temp[tuple(key)]=True
                    count+=traverse(i,j,[])          
        return count+n
        """