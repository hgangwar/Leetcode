class Solution(object):
    def captureForts(self, forts):
        l=len(forts)
        captured,b_captured, max_captured=0,0,0
        moving,b_moving=0,0
        for i in range(0,l):
            #moving forward 
            if (moving==1 and forts[i]==-1):
                #moving completed
                moving=0
                captured=i-start-1
                max_captured=max(captured,max_captured)
            if (moving==1 and forts[i]!=0):
                #moving distrubed
                moving=0
            if (moving==0 and forts[i]==1):
                #moving starts
                moving=1
                start=i
                
            
            
        for i in range(0,l):
            #moving backwards
            if (b_moving==1 and forts[i]==1):
                #moving completed
                b_moving=0
                b_captured=i-b_start-1
                max_captured=max(b_captured,max_captured)
            if (b_moving==1 and forts[i]!=0):
                #moving distrubed
                b_moving=0
                
            if (b_moving==0 and forts[i]==-1):
                #moving starts
                b_moving=1
                b_start=i   
            
        return max_captured         
if __name__ == "__main__":
    obj=Solution()
    Op=obj.captureForts([1,0,0,-1,0,0,-1,0,0,1])
    print(Op)
