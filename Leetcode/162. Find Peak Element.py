class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)-1
        nums.append(-2**31 - 1)
        def binsearch(start,end):
            if(end<start):
                return -1
            mid=int((start+end)//2)
            if (start==end):
                if(nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]):
                    return mid
                return -1
            if(nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]):
                return mid
            if(mid>0):
                K=binsearch(start,mid-1)
                if K!=-1:
                    return K
            if(mid<n):
                K=binsearch(mid+1,end)
                if K!=-1:
                    return K
            return -1
             
        return binsearch(0,n)
if __name__ == "__main__":
    obj=Solution()
    nums = [1,2,3,1]
    Op=obj.findPeakElement(nums)
    print(Op)
