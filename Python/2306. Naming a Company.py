from collections import defaultdict
class Solution(object):
    def distinctNames(self, ideas):
        Alpa=defaultdict(set)
        for x in ideas:
            if len(x)>1: Alpa[x[0]].add(x[1:])
            else: Alpa[x[0]].add("")
        Ans=0
        Bets=list(Alpa.keys())
        for i,x in enumerate(Bets):
            for y in range(i+1,len(Bets)):
                Inter=Alpa[x].intersection(Alpa[Bets[y]])
                n1,n2=len(Alpa[x]),len(Alpa[Bets[y]])
                Ans+=(n1-len(Inter))*(n2-len(Inter))
        return 2*Ans
if __name__ == "__main__":
    obj=Solution()
    Op=obj.distinctNames(ideas = ["coffee","donuts","time","toffee"])
    print(Op)