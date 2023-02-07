class Solution(object):
    def search(self,islands,key,block=[]):
        key=tuple(key)
        block=block+[key]
        if not (key in islands):
            return block
        for x in islands[key]:
            if not tuple(x) in block:
                block=self.search(islands,x,block)                
        return block
    def maxAreaOfIsland(self, grid):
        r,c,flag=len(grid),len(grid[0]),0
        islands=dict()
        for i in range(r):
            for j in range(c):
                key=tuple([i,j])
                if(grid[i][j]==0):
                    continue
                flag=1
                if i>=1:
                    if grid[i-1][j]==grid[i][j]:
                        if not key in islands:
                            islands[key]=[[i-1,j]]
                        else:
                            islands[key]+=[[i-1,j]]

                if i+1<r:
                    if grid[i+1][j]==grid[i][j]:
                        if not key in islands:
                            islands[key]=[[i+1,j]]
                        else:
                            islands[key]+=[[i+1,j]]
                if j>=1:
                    if grid[i][j-1]==grid[i][j]:
                        if not key in islands:
                            islands[key]=[[i,j-1]]
                        else:
                            islands[key]+=[[i,j-1]]
                if j+1<c:
                    if grid[i][j+1]==grid[i][j]:
                        if not key in islands:
                            islands[key]=[[i,j+1]]
                        else:
                            islands[key]+=[[i,j+1]]
        
        P_nodes=islands.keys()
        if(len(P_nodes)==0):
            return flag
        max_area,area=0,0
        check=dict()
        for x in P_nodes:
            if not x in check:
                block=self.search(islands,x,[])
                area=len(block)
                max_area=max(area,max_area)
                for x in block:
                    check[x]=True            
        return max_area

if __name__ == "__main__":
    obj=Solution()
    grid = [[1]]
    Op=obj.maxAreaOfIsland(grid)
    print(Op)
