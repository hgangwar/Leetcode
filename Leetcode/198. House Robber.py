class Solution(object):
    def rob(self, nums):
        l=len(nums)
        if(l<3):
            return max(nums)
        if(l==3):
            return max(nums[1], nums[0]+nums[2])
        Sums=[0]*l
        Sums[0], Sums[1]=nums[0], nums[1]
        Sums[2]=nums[0]+nums[2]
        for i in range(2, l):
            Sums[i]=max(Sums[i-2], Sums[i-3])+nums[i]
        return max(Sums[l-3:l])
if __name__ == "__main__":
    obj=Solution()
    nums = [1,2,3,1]
    Op=obj.rob(nums)
    print(Op)
