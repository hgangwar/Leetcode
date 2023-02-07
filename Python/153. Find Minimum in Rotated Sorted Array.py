class Solution(object):
    def findMin(self, nums):
        if(len(nums)<=3):
            return min(nums)
        start,end,mid,flag=0,len(nums)-1,0,0
        while(end-start>1):
            mid=int((start+end)//2)
            if(nums[mid-1]>nums[mid]):
                flag=1
                break
            if(nums[mid]<nums[start]):
                end=mid
            elif(nums[mid]>nums[start]):
                end=mid
        if(flag==0):
            return min(nums[start],nums[end])
        return nums[mid]
if __name__ == "__main__":
    obj=Solution()
    nums = [11,13,15,17]
    Op=obj.findMin(nums)
    print(Op)
