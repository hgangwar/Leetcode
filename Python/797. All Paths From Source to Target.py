class Solution(object):
    def dfs(self,graph,start,end,path=[], track=[]):
        localpath=[]
        localpath+=[start]
        if( start==end):
            track+=[path+localpath]
            return track
        for x in graph[start]:
            track=self.dfs(graph,x,end,path+localpath,track)            
        return track  
    def allPathsSourceTarget(self, graph):
        n=len(graph)
        paths=self.dfs(graph,0,n-1,[])             
        return paths

if __name__ == "__main__":
    obj=Solution()
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Op=obj.allPathsSourceTarget(graph)
    print(Op)
