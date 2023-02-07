#BFS with path return
class Solution(object):
    def bfs(self, graph, grid, ndx, Time):
        r,c=len(grid),len(grid[0])
        queue, visited=[],[False]*(r*c)
        queue.append([ndx])
        while(queue):
            path=queue.pop(0)
            node=path[-1]
            if visited[node]==False:
                visited[node]=True
                for x in graph[node]:
                    newpath=list(path)
                    newpath.append(x)
                    queue.append(newpath)
                    i,j=x//c,x%c
                    Time[i][j]=min(Time[i][j],len(newpath)-1)                    
        return Time

    def orangesRotting(self, grid):
        r,c=len(grid),len(grid[0])
        Time=[[2**10 for i in range(c)] for j in range(r)]
        graph=dict()
        Vertex=[]
        for i in range(r):
            for j in range(c):
                if(grid[i][j]==0):
                     Time[i][j]=-5
                     continue
                if(grid[i][j]==2):
                     Time[i][j]=0
                     Vertex.append([i,j])
                key=(i*c)+j
                graph[key]=[]
                if(i>0):                    
                    if(grid[i-1][j]!=0):
                        graph[key]+=[(i-1)*c+j]
                if(i<r-1):
                    if(grid[i+1][j]!=0):
                        graph[key]+=[(i+1)*c+j]
                if(j>0):
                    if(grid[i][j-1]!=0):
                        graph[key]+=[(i*c)+j-1]
                if(j<c-1):
                    if(grid[i][j+1]!=0):
                        graph[key]+=[(i*c)+j+1]
        for x in Vertex:
            ndx=(x[0]*c)+x[1]
            Time=self.bfs(graph,grid,ndx,Time)
        Max=0
        for x in Time:
            Max=max(Max,max(x))
        if(Max==2**10):
            return -1
        else:
            return Max

if __name__ == "__main__":
    obj=Solution()
    grid =[[2,1,1],[1,1,0],[0,1,1]]
    Op=obj.orangesRotting(grid)
    print(Op)
