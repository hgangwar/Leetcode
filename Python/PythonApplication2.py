from tempfile import tempdir
import tempfile
import numpy as np

class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        l, r=0, len(nums)-1
        nums=nums[::-1]
        l, r=0, k-1
        nums[0:r+1]=nums[r::-1]
        l, r=k,len(nums)-1
        nums[k:r+1]=nums[r:l-1:-1] 
        
        return nums
if __name__ == "__main__":
    obj=Solution()
    Op=obj.rotate([5,6,7,1,2,3,4],2)
    print(Op)