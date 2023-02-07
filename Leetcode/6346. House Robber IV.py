import heapq
class Solution(object):
    def minCapability(self, nums, k):
        if len(nums)<3 or k==1: return min(nums)
        PPP,PP,P=[nums[0]],[nums[1]],[]
        n=len(nums)
        if n==3: return min(nums[0], nums[2])
        P=[min(nums[0], nums[2]),max(nums[0], nums[2])]
        i=3
        Curr=[]
        while(i<n):
            if len(Curr)==k:
                if (nums[i]<Curr[-1]):
                    Curr[-1]=nums[i]
            elif len(Curr)<k:
                if PP[-1]<=PPP[-1]:
                    Curr=PP[:]
                    Curr.append(nums[i])
                else:
                    Curr=PPP[:]
                    Curr.append(nums[i])
            Curr.sort()
            PPP=PP[:]
            PP=P[:]
            P=Curr[:]
            i+=1
        Min=1e09
        if len(PP)!=k:
            Min=max(P)
        else:
            Min=min(max(PP), max(P))
        return  Min          
            

if __name__ == "__main__":
    obj=Solution()
    Op=obj.minCapability([35,9,18,78,40,8,71,2,59], 5)
    print(Op)