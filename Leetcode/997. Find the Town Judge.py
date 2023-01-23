from collections import defaultdict
class Solution(object):
    def findJudge(self, n, trust):
        if not trust and n==1: return 1
        if not trust: return -1
        Map=defaultdict(list)
        for x in trust:
            Map[x[0]]+=[x[1]]
        res=set(Map[trust[0][0]])
        if (len(Map.keys())<n-1): return -1
        for x in Map.keys():
            Curr=set(Map[x])
            res=res.intersection(Curr)
            if not res: return -1
        if (len(res)>1): return -1
        res=tuple(res)
        res=res[0]
        if (res in Map): return -1
        return res
if __name__ == "__main__":
    obj=Solution()
    Op=obj.findJudge(4,[[1,3],[1,4],[2,3]])
    print(Op)