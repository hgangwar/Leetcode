class Solution(object):
    def search(self, nums, target):
        if(len(nums)<=3):
            for i in range(len(nums)):
                if(target==nums[i]): return i
            return -1 
        start,end,mid,flag=0,len(nums)-1,0,0
        while(end-start>1):
            mid=int((start+end)//2)
            if(nums[mid-1]>nums[mid]):
                flag=1
                break
            if(nums[mid]>nums[mid+1]):
                flag=1
                mid+=1
                break
            if(nums[mid]<nums[start]):
                end=mid-1
            elif(nums[mid]>nums[start]):
                start=mid+1
        if(flag==0):
            if(nums[end]<nums[start]): mid=end
        if(target>=nums[mid] and target<=nums[-1]):
            start, end=mid, len(nums)-1
        elif(target>=nums[0] and target<=nums[mid-1]):
            start,end=0,mid-1
        else:
            return -1
        while(start<=end):
            mid=int((start+end)//2)
            if(nums[mid]==target):
                return mid
            if(nums[mid]>target):
                end=mid-1
            elif(nums[mid]<target):
                start=mid+1
        return -1

if __name__ == "__main__":
    obj=Solution()
    nums = [8,1,2,3,4,5,6,7]
    target = 1
    Op=obj.search(nums,target)
    print(Op)
