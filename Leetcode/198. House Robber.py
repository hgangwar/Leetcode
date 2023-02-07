class Solution(object):
    def rob(self, nums):
        l=len(nums)
        if(l==0):
            return 0
        PPP, PP,P=0, 0, 0
        for i in range(0, l):
            Curr=max(PP,PPP)+nums[i]
            PPP=PP
            PP=P
            P=Curr
        return max(P,PP)
if __name__ == "__main__":
    obj=Solution()
    nums = [1,2,3,1]
    Op=obj.rob(nums)
    print(Op)
