from collections import Counter
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.e = 0

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def give_Parents(self, n):
        for i in range(n):
            self.p[i]=self.find(i)
        return self.p

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
        
class Solution(object):
    def countPairs(self, n, edges):
        UF = DSU(n)
        for x in edges:
            UF.union(x[1],x[0])
        Parents=UF.give_Parents(n)
        Count=Counter()
        Ans=0
        for x in Parents:
            Count[x]+=1
        for _,val in Count.items():
            Ans+=(val*(n-val))
        return int(Ans/2)

if __name__ == "__main__":
    obj=Solution()
    n=12
    edges=[[2,6],[11,3],[5,4],[9,6]] 
    Op=obj.countPairs(n,edges)
    print(Op)