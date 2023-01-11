class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n,tank,i,low,ndx=len(gas),0,0,1000000,0
        while(i<n):
            tank+=(gas[i]-cost[i])
            if(tank<=low):
                ndx=i
                low=tank
            i+=1
        if(tank>=0): return (ndx+1)%n
        return -1
if __name__ == "__main__":
    obj=Solution()
    gas = [11,4,7,1,0]
    cost = [2,5,5,9,1]

    Op=obj.canCompleteCircuit(gas,cost)
    print(Op)
