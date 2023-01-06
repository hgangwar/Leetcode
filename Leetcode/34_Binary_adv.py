class Solution(object):
    def searchRange(self, nums, target):
        if(len(nums)==0):
            return [-1,-1]
        start,end=0,len(nums)-1
        mid, flag=int(end//2),0
        while(end-start>1):
            if(nums[mid]==target):
                front,back=0,0
                start,end, Mid=0,mid,int(mid//2)
                while(end-start>1):
                    if(nums[Mid]==target):
                        end=Mid
                    else:
                        start=Mid
                    Mid=int((start+end)//2)
                if(nums[start]==target):
                    back=start
                else:
                    back=end
                start,end, Mid=mid,len(nums)-1,int((mid+len(nums)-1)//2)
                while(end-start>1):
                    if(nums[Mid]==target):
                        start=Mid
                    else:
                        end=Mid
                    Mid=int((start+end)//2)
                if(nums[end]==target):
                    front=end
                else:
                    front=start
                return [back, front]
            elif(nums[mid]<target):
                start=mid
            else:
                end=mid
            mid=int((start+end)//2)
        if(flag!=1):
            if(nums[start]==target):
                return [start, start]
            elif(nums[end]==target):
                return [end,end]
            else:
                return [-1 , -1]
if __name__ == "__main__":
    obj=Solution()
    nums = [10]
    target = 10
    Op=obj.searchRange(nums,target)
    print(Op)
