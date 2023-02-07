from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        pre_sum,res=0,0
        graph=defaultdict(int)
        graph[0]+=1  
        for i in range(len(nums)):
            pre_sum=pre_sum+nums[i]
            mod=pre_sum%k
            if mod<0: mod+=k
            res+=graph[mod]
            graph[mod]+=1
        return res
if __name__ == "__main__":
    obj=Solution()
    nums = [1,-10,5]
    k = 9
    Op=obj.subarraysDivByK(nums,k)
    print(Op)
"""
Naive solution: O(n.n)
class Solution(object):
    def subarraysDivByK(self, nums, k):
        n=len(nums)
        pre_sum=[0]*(n+1)
        res=0
        pre_sum[0]=0
        for i in range(len(nums)):
            pre_sum[i+1]=pre_sum[i]+nums[i]
        for i in range(n+1):
            for j in range(0,i):
                if(pre_sum[i]-pre_sum[j])%k==0: res+=1           
        return res

"""