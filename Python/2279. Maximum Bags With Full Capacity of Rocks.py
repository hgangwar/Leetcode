class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        for i in range(len(capacity)):
            capacity[i]-=rocks[i]
        capacity.sort()
        count,i=0,0
        while(additionalRocks>0 and i<len(rocks)):
            additionalRocks-=capacity[count]
            if(additionalRocks>=0):
                count+=1
            i+=1
        return count
if __name__ == "__main__":
    obj=Solution()
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    Op=obj.maximumBags(capacity, rocks, additionalRocks)
    print(Op)
