class Solution(object):    
    def smallestEquivalentString(self, s1, s2, baseStr):
        graph=dict()
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            if s1[i] in graph:
                graph[s1[i]]+=s2[i]
            else:
                graph[s1[i]]=s2[i]
            if(s2[i]in graph):
                graph[s2[i]]+=s1[i]
            else:
                graph[s2[i]]=s1[i]
        Op=[]
        def dfs(src,val,visited,graph):
            visited[ord(src)-97]=True
            val=min(val,src)
            for x in graph[src]:
                if not visited[ord(x)-97]:
                    val=dfs(x,val,visited,graph)
            return val
        for x in baseStr:
            if x in graph:
                temp=dfs(x,"z",[False]*26,graph)
                Op.append(temp)
            else:
                Op.append(x)
        Op=''.join(Op)
        return Op
if __name__ == "__main__":
    obj=Solution()
    s1 = "ceihfgechfcbjhadaibhghcbdhfaecdaijigaaafcadebciabb"
    s2 = "gafbfceidigjceeigcddichdhhbgibjbaagbfciiecjaiajahh"
    baseStr = "eoiloytuagirigmbarebhzgveiavyruxlrxzbommyfjjngfktd"
    Op=obj.smallestEquivalentString(s1,s2,baseStr)
    print(Op)

