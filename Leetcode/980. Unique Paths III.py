class Solution(object):
    def near(self,i,j,r,c):
        ls=[]
        if(j>0):
            ls+=[[i,j-1]]
        if(j<c-1):
            ls+=[[i,j+1]]
        if(i>0): 
            ls+=[[i-1,j]]
        if(i<r-1):
            ls+=[[i+1,j]]        
        return ls
    def bfs(self, grid, start,cells):
        r,c=len(grid),len(grid[0])
        queue,count=[],0
        queue.append([start])
        while(queue):
            path=queue.pop(0)            
            node=path[-1]
            if(len(path)!=len(set(path)) or grid[node//c][node%c]==2):
               continue            
            visited=[False]*(r*c)
            l=len(path)
            for i in range(l-1):
                visited[path[i]]=True
            if visited[node]==False:
                visited[node]=True
                Nb=self.near(node//c,node%c,r,c)
                l,i=len(Nb),0
                while(i<l):
                    x=Nb[i]
                    if not (grid[x[0]][x[1]]==0 or grid[x[0]][x[1]]==2):
                        Nb.pop(i)
                        l-=1
                    else:
                        i+=1
                for x in Nb:
                    i,j=x[0],x[1]
                    newpath=list(path)
                    newpath.append((i*c)+j)
                    queue.append(newpath)
                    if(grid[i][j]==2 ):
                        if( len(newpath)==cells):
                            count+=1                   
        return count
    def uniquePathsIII(self, grid):
        r,c=len(grid),len(grid[0])
        start, cells=-1,0
        for i in range(r):
            for j in range(c):
                if(grid[i][j]!=-1):
                    cells+=1
                if(grid[i][j]==1):
                    start=(i*c)+j
        count=self.bfs(grid,start,cells)
        return count
if __name__ == "__main__":
    obj=Solution()
    grid =[[-1,-1,0,-1],[1,0,0,0],[0,-1,0,0],[-1,-1,0,-1],[2,0,0,-1]]
    Op=obj.uniquePathsIII(grid)
    print(Op)