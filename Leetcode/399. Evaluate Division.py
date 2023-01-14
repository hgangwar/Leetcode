class Solution(object):
    def dfs(self,Map,start,end,path=[]):
        localpath=[]
        localpath+=[start]
        if( start==end):
            return path+localpath
        for x in Map[start]:
            newpath=[[-1]]
            if not x[0] in path:
                newpath=self.dfs(Map,x[0],end,path+localpath)
            if(newpath==None): continue
            if (newpath[-1]==end):
                return newpath
        return None
    def calcEquation(self, equations, values, queries):
        Map=collections.defaultdict(list)
        Table=dict()
        n=len(equations)
        def valueP(Path):
            if(Path==None):
                return -1
            elif(len(Path)==1):
                return 1
            else:
                value=1
                for x in range(1,len(Path)):
                    value=value*Table[Path[x-1],Path[x]]
                return value
        for i,x in enumerate(equations):
            Map[x[0]]+=[[x[1],values[i]]]
            Table[x[0],x[1]]=values[i]
            Map[x[1]]+=[[x[0],1/values[i]]]
            Table[x[1],x[0]]=1/values[i]
        Op=[-1]*len(queries)
        for I,X in enumerate(queries):
            [C,D]=X
            if C in Map and D in Map:
                SP=self.dfs(Map,C,D)
                Op[I]=valueP(SP)
        return Op