class Solution(object):
    def search(self,fill,key,flood=[]):
        key=tuple(key)
        flood=flood+[key]
        if not (key in fill):
            return flood
        for x in fill[key]:
            if not tuple(x) in flood:
                flood=self.search(fill,x,flood)
                
        return flood
    def floodFill(self, image, sr, sc, color):
        r,c=len(image),len(image[0])
        fill=dict()
        if(image[sr][sc]==color):
            return image
        for i in range(r):
            for j in range(c):
                key=tuple([i,j])
                if i>=1:
                    if image[i-1][j]==image[i][j]:
                        if not key in fill:
                            fill[key]=[[i-1,j]]
                        else:
                            fill[key]+=[[i-1,j]]

                if i+1<r:
                    if image[i+1][j]==image[i][j]:
                        if not key in fill:
                            fill[key]=[[i+1,j]]
                        else:
                            fill[key]+=[[i+1,j]]
                if j>=1:
                    if image[i][j-1]==image[i][j]:
                        if not key in fill:
                            fill[key]=[[i,j-1]]
                        else:
                            fill[key]+=[[i,j-1]]
                if j+1<c:
                    if image[i][j+1]==image[i][j]:
                        if not key in fill:
                            fill[key]=[[i,j+1]]
                        else:
                            fill[key]+=[[i,j+1]]
        
        if not (tuple([sr,sc]) in fill):
            image[sr][sc]=color
            return image
        
        flood=self.search(fill,tuple([sr,sc]),[])
        
        for x in flood:
            x=list(x)
            image[x[0]][x[1]]=color
        return image       
        
if __name__ == "__main__":
    obj=Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2    
    Op=obj.floodFill(image,sr,sc,color)
    print(Op)
