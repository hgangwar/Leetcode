class Solution(object):
    def minimumTotal(self, triangle):
        r=len(triangle)
        Pre=[]
        Pre.append(triangle[0][0])
        for i in range(1,r):
            new=[]
            new.append(Pre[0]+triangle[i][0])
            for j in range(1,i):
                element=triangle[i][j]
                p1=Pre[j-1]+element
                p2=Pre[j]+element
                new.append(min(p1,p2))
            new.append(Pre[-1]+triangle[i][-1])
            Pre=new
        Min=min(Pre)
        return Min
if __name__ == "__main__":
    obj=Solution()
    triangle = [[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]
    Op=obj.minimumTotal(triangle)
    print(Op)
""" Naive graph solution
 class Solution(object):
    def bfs(self, r, ndx, level, path=[], track=[]):
        local=[]
        local.append(ndx)
        if(level==r):
            temp=path+local
            track.append(path+local)
            return track         
        if (ndx[1]<=level and ndx[0]+1<=r):            
            track=self.bfs(r,[ndx[0]+1,ndx[1]],level+1,path+local,track)
            track=self.bfs(r,[ndx[0]+1,ndx[1]+1],level+1,path+local,track)        
        return track
    def minimumTotal(self, triangle):
        r=len(triangle)
        paths=self.bfs(r,[1,1],1,[],[])
        Min=2**20
        for path in paths:
            Sum=0
            for x in path:
                Sum+=triangle[x[0]-1][x[1]-1]
            Min=min(Sum,Min)
        return Min
        """
