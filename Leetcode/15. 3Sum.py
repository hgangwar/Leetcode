class Solution(object):
    def threeSum(self, nums):
        nums.sort()             
        n=len(nums)
        Map=dict()
        Op=[]
        for x in nums:
            Map[x]=[4000,0]
        for i,x in enumerate(nums):
            y=Map[x]
            Map[x]=[min(y[0],i),y[1]+1]
        Keys=list(Map.keys())
        Keys.sort()
        if( 0 in Keys):
            if(Map[0][1]>2):
                Op.append([0,0,0])
        if(len(Keys)<3):
            return Op            
        back, front,n=0,1,len(Keys)
        while(front<n):
            B,F=Keys[back],Keys[front]
            Sum=-(B+F)
            if (Sum) in Map:
                [ndx,count]=Map[Sum]
                if(count>1 or (ndx!=Map[B][0] and ndx!=Map[F][0])):
                    ls=[B, -(B+F), F]
                    ls.sort()
                    Op.append(tuple(ls))
            front+=1
            if(front==n):
                back+=1
                front=back+1
        Op=set(Op)
        Op=[list(i) for i in Op]
        return Op
if __name__ == "__main__":
    obj=Solution()
    nums = [0,0,0]
    Op=obj.threeSum(nums)
    print(Op)
