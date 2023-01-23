class Solution(object):
    def maxSubarraySumCircular(self, nums):
        n=len(nums)
        Max_H,Max_S=0,-4e5
        DP, CF=[nums[0]]*n,[nums[0]]*n
        for x in (nums):       
            Max_H+=x
            if(Max_H>Max_S):
                Max_S=Max_H
            if(Max_H<0):
                Max_H=0
        for i in range(1,n):
            CF[i]=CF[i-1]+nums[i]
            DP[i]=max(DP[i-1],CF[i])
        for i in range(1,n):
            Max_S=max(Max_S, DP[i]+CF[-1]-CF[i])     
        return Max_S
if __name__ == "__main__":
    obj=Solution()
    nums = [5,-3,5]
    Op=obj.maxSubarraySumCircular(nums)
    print(Op)
