class Solution(object):
    def summaryRanges(self, nums):
        intervals=[]
        i,flag=0,True
        nums.append(-3)
        while(i<len(nums)-1):
            if flag: 
                front=nums[i]
                flag=False
            if (nums[i]!=nums[i+1]-1):
                if nums[i]==nums[i+1]-1:
                    end=nums[i+1]
                else: end=nums[i]
                if front==end:
                    intervals.append(str(nums[i]))
                else:
                    intervals.append(str(front)+"->"+str(end))
                flag=True
            i+=1
        return intervals        
if __name__ == "__main__":
    obj=Solution()
    Op=obj.summaryRanges([0,2,3,4,6,8,9])
    print(Op)