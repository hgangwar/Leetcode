class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        ans,Sum=0,0
        while(ans<len(costs)):
            Sum+=costs[ans]
            if(Sum<=coins):
                ans+=1
            else:
                return ans
        return ans
if __name__ == "__main__":
    obj=Solution()
    costs = [1,3,2,4,1]
    coins = 7
    Op=obj.maxIceCream(costs,coins)
    print(Op)

